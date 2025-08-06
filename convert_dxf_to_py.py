import ezdxf
import os
import re


def sanitize_filename(name):
    return re.sub(r'[^\w\-_.]', '_', name)


def entity_to_code(entity):
    if entity.dxftype() == "LINE":
        start = entity.dxf.start
        end = entity.dxf.end
        return f'    msp.add_line(({start.x}, {start.y}), ({end.x}, {end.y}))'

    elif entity.dxftype() == "CIRCLE":
        center = entity.dxf.center
        radius = entity.dxf.radius
        return f'    msp.add_circle(({center.x}, {center.y}), {radius})'

    elif entity.dxftype() == "ARC":
        center = entity.dxf.center
        radius = entity.dxf.radius
        start_angle = entity.dxf.start_angle
        end_angle = entity.dxf.end_angle
        return f'    msp.add_arc(({center.x}, {center.y}), {radius}, {start_angle}, {end_angle})'

    elif entity.dxftype() == "TEXT":
        insert = entity.dxf.insert
        text = entity.dxf.text
        height = entity.dxf.height
        return f'    msp.add_text("{text}", dxfattribs={{"height": {height}, "insert": ({insert.x}, {insert.y})}})'

    else:
        return f'    # Unsupported entity type: {entity.dxftype()}'


def export_block_to_py(block, output_dir):
    block_name = sanitize_filename(block.name)
    filename = os.path.join(output_dir, f"{block_name}.py")

    if os.path.exists(filename):
        print(f"⚠️ File {filename} đã tồn tại, bỏ qua.")
        return

    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Generated block drawing as Python module\n")
        f.write("def add_to_drawing(msp):\n")

        for entity in block:
            code = entity_to_code(entity)
            f.write(code + "\n")

    print(f"Exported block '{block.name}' to {filename}")


def extract_blocks_from_dxf(input_file_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    doc = ezdxf.readfile(input_file_path)
    count = 0
    for block in doc.blocks:
        if not block.name.startswith("*"):
            export_block_to_py(block, output_dir)
            count += 1

    print(f"Đã trích xuất {count} block từ '{input_file_path}' vào '{output_dir}'.")


if __name__ == "__main__":
    input_dxf_path = r"E:\pythonProject\pythonProject1\test_picture\process_80.dxf"
    output_block_dir = r"E:\pythonProject\pythonProject1\test_picture\component_lib\block11"

    extract_blocks_from_dxf(input_dxf_path, output_block_dir)
