# convert_to_block_lib.py
import ezdxf
import os
import re

def sanitize_filename(name):
    return re.sub(r'[^\w\-_.]', '_', name)

# Lấy doc an toàn (compat nhiều phiên bản ezdxf)
def _get_doc_from_layout(layout):
    return getattr(layout, "doc", None) or getattr(layout, "drawing", None)

# --- Giữ màu layer từ DXF gốc
def get_layer_color(block, layer_name):
    try:
        doc = _get_doc_from_layout(block)
        return int(doc.layers.get(layer_name).color)
    except Exception:
        return 7  # fallback ACI

def collect_layers_of_block(block):
    layers = {}
    for e in block:
        try:
            lyr = e.dxf.layer
        except Exception:
            lyr = "0"
        if lyr not in layers:
            layers[lyr] = {"color": get_layer_color(block, lyr)}
    return layers

def _attrs_for(entity):
    # Luôn giữ layer; nếu entity set màu trực tiếp (khác BYBLOCK/BYLAYER) thì giữ luôn
    try:
        layer = entity.dxf.layer
    except Exception:
        layer = "0"
    try:
        ent_color = int(entity.dxf.color)
    except Exception:
        ent_color = None

    parts = [f'"layer": "{layer}"']
    if ent_color not in (None, 0, 256):  # 0=BYBLOCK, 256=BYLAYER
        parts.append(f'"color": {ent_color}')
    # trả về chuỗi key:value (không có { })
    return ", ".join(parts)

def entity_to_code(entity, tgt="msp"):
    A = _attrs_for(entity)

    if entity.dxftype() == "LINE":
        start = entity.dxf.start
        end = entity.dxf.end
        return (
            f'    {tgt}.add_line(({start.x}, {start.y}), ({end.x}, {end.y}), '
            f'dxfattribs={{ {A} }})'
        )

    elif entity.dxftype() == "CIRCLE":
        center = entity.dxf.center
        radius = entity.dxf.radius
        return f'    {tgt}.add_circle(({center.x}, {center.y}), {radius}, dxfattribs={{ {A} }})'

    elif entity.dxftype() == "ARC":
        center = entity.dxf.center
        radius = entity.dxf.radius
        start_angle = entity.dxf.start_angle
        end_angle = entity.dxf.end_angle
        return (
            f'    {tgt}.add_arc(({center.x}, {center.y}), {radius}, '
            f'{start_angle}, {end_angle}, dxfattribs={{ {A} }})'
        )

    elif entity.dxftype() == "TEXT":
        insert = entity.dxf.insert
        text = str(entity.dxf.text).replace('"', '\\"')
        height = entity.dxf.height
        return (
            f'    {tgt}.add_text("{text}", dxfattribs={{"height": {height}, '
            f'"insert": ({insert.x}, {insert.y}), {A}}})'
        )

    else:
        return f'    # Unsupported entity type: {entity.dxftype()}'

def export_block_to_py(block, output_dir):
    file_stem = sanitize_filename(block.name)
    filename = os.path.join(output_dir, f"{file_stem}.py")

    if os.path.exists(filename):
        print(f"⚠️ File {filename} đã tồn tại, bỏ qua.")
        return

    # Thu thập layer & màu từ DXF gốc
    layers_map = collect_layers_of_block(block)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Generated block drawing as Python module (keep layer color & real block name)\n")
        # Lưu tên block gốc
        f.write(f'BLOCK_NAME = r"{block.name}"\n')
        # Bảng layer-color
        f.write("LAYERS = {\n")
        for lyr, attrs in layers_map.items():
            f.write(f'    "{lyr}": {{"color": {attrs.get("color", 7)}}},\n')
        f.write("}\n\n")

        # Helper: lấy doc & đảm bảo layer tồn tại với đúng màu
        f.write("def _get_doc(layout):\n")
        f.write("    return getattr(layout, 'doc', None) or getattr(layout, 'drawing', None)\n\n")

        f.write("def _ensure_layers(doc):\n")
        f.write("    for name, attrs in LAYERS.items():\n")
        f.write("        if name in doc.layers:\n")
        f.write("            lay = doc.layers.get(name)\n")
        f.write("            if 'color' in attrs:\n")
        f.write("                lay.color = attrs['color']\n")
        f.write("        else:\n")
        f.write("            doc.layers.new(name, dxfattribs={'color': attrs.get('color', 7)})\n\n")

        # Vẽ vào layout bất kỳ
        f.write("def _draw_into(layout):\n")
        for entity in block:
            f.write(entity_to_code(entity, tgt="layout") + "\n")
        f.write("\n")

        # Giữ nguyên cách cũ: vẽ trực tiếp primitive (không có blockref)
        f.write("def add_to_drawing(msp):\n")
        f.write("    _doc = _get_doc(msp)\n")
        f.write("    if _doc is not None:\n")
        f.write("        _ensure_layers(_doc)\n")
        f.write("    _draw_into(msp)\n\n")

        # NEW: tạo block definition đúng tên gốc
        f.write("def register_block(doc):\n")
        f.write("    _ensure_layers(doc)\n")
        f.write("    if BLOCK_NAME in doc.blocks:\n")
        f.write("        blk = doc.blocks.get(BLOCK_NAME)\n")
        f.write("        # Xoá nội dung cũ? Không: giữ nguyên để an toàn.\n")
        f.write("    else:\n")
        f.write("        blk = doc.blocks.new(name=BLOCK_NAME)\n")
        f.write("    _draw_into(blk)\n\n")

        # NEW: chèn blockref để DXF có BLOCK/INSERT (có block name thật)
        f.write("def insert_block(msp, insert=(0, 0), rotation_deg=0, scale=1.0, layer='0'):\n")
        f.write("    doc = _get_doc(msp)\n")
        f.write("    if doc is None:\n")
        f.write("        raise RuntimeError('Không lấy được document từ layout.')\n")
        f.write("    if BLOCK_NAME not in doc.blocks:\n")
        f.write("        register_block(doc)\n")
        f.write("    ref = msp.add_blockref(BLOCK_NAME, insert, dxfattribs={'layer': layer})\n")
        f.write("    try:\n")
        f.write("        ref.dxf.rotation = rotation_deg\n")
        f.write("        ref.dxf.xscale = scale\n")
        f.write("        ref.dxf.yscale = scale\n")
        f.write("    except Exception:\n")
        f.write("        pass\n")

    print(f"✅ Exported block '{block.name}' to {filename}")

def extract_blocks_from_dxf(input_file_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    doc = ezdxf.readfile(input_file_path)
    count = 0
    for block in doc.blocks:
        if not block.name.startswith("*"):  # bỏ qua anonymous blocks
            export_block_to_py(block, output_dir)
            count += 1

    print(f"\n🎉 Đã trích xuất {count} block từ '{input_file_path}' vào '{output_dir}'.")

if __name__ == "__main__":
    input_dxf_path = r"E:\pythonProject\pythonProject1\test_picture\output_final23.dxf"
    output_block_dir = r"E:\pythonProject\pythonProject1\test_picture\component_lib\block37"
    extract_blocks_from_dxf(input_dxf_path, output_block_dir)
