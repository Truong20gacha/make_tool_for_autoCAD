import ezdxf
import os
import re
import json


def sanitize_filename(name):
    return re.sub(r'[^\w\-_.]', '_', name)


def _get_doc_from_layout(layout):
    return getattr(layout, "doc", None) or getattr(layout, "drawing", None)


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


def _attrs_dict(entity):
    d = {}
    try:
        d["layer"] = entity.dxf.layer
    except Exception:
        d["layer"] = "0"
    try:
        ent_color = int(entity.dxf.color)
        if ent_color not in (None, 0, 256):
            d["color"] = ent_color
    except Exception:
        pass
    return d


def entity_to_json(entity, offset_x=0.0, offset_y=0.0):
    def ox(x): return round(x + offset_x, 6)
    def oy(y): return round(y + offset_y, 6)

    typ = entity.dxftype()
    attribs = _attrs_dict(entity)
    data = {"type": typ, "attribs": attribs}

    if typ == "LINE":
        start = entity.dxf.start
        end = entity.dxf.end
        data["pointsd"] = [ox(start.x), oy(start.y), ox(end.x), oy(end.y)]
    elif typ == "TEXT":
        insert = entity.dxf.insert
        data["text"] = str(entity.dxf.text)
        data["insert"] = [ox(insert.x), oy(insert.y)]
        data["height"] = entity.dxf.height
    else:
        # fallback: lưu raw_code nếu chưa hỗ trợ
        data["raw_code"] = entity.dxftype()

    return data


def get_block_bbox(block):
    min_x = min_y = float("inf")
    max_x = max_y = float("-inf")
    has_entity = False
    for e in block:
        try:
            box = e.bbox()
            (x1, y1, _), (x2, y2, _) = box.extmin, box.extmax
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            has_entity = True
        except Exception:
            continue
    if not has_entity:
        return None
    return min_x, min_y


def export_block_to_json(block, output_dir):
    file_stem = sanitize_filename(block.name)
    filename = os.path.join(output_dir, f"{file_stem}.json")
    if os.path.exists(filename):
        print(f"⚠️ File {filename} đã tồn tại, bỏ qua.")
        return

    bbox = get_block_bbox(block)
    if bbox:
        min_x, min_y = bbox
        offset_x, offset_y = -min_x, -min_y
    else:
        offset_x = offset_y = 0.0

    layers_map = collect_layers_of_block(block)

    entities_data = []
    for entity in block:
        entities_data.append(entity_to_json(entity, offset_x, offset_y))

    block_data = {
        "BLOCK_NAME": block.name,
        "LAYERS": layers_map,
        "entities": entities_data
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(block_data, f, indent=2, ensure_ascii=False)

    print(f"✅ Exported block '{block.name}' to {filename}")


def extract_blocks_from_dxf(input_file_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    doc = ezdxf.readfile(input_file_path)
    count = 0
    for block in doc.blocks:
        if not block.name.startswith("*"):
            export_block_to_json(block, output_dir)
            count += 1
    print(f"\n🎉 Đã trích xuất {count} block từ '{input_file_path}' vào '{output_dir}'.")


if __name__ == "__main__":
    input_dxf_path = r"E:\pythonProject\pythonProject1\test_picture\compare_blocks.dxf"
    output_block_dir = r"E:\pythonProject\pythonProject1\test_picture\component_lib\block63"
    extract_blocks_from_dxf(input_dxf_path, output_block_dir)
