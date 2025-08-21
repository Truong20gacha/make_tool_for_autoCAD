import ezdxf
import csv
import re
import importlib
import component_lib.block10  # thư viện chứa các block


def sanitize_name(name):
    return re.sub(r'[^\w\-_.]', '_', name)


def run_block_module_with_offset(block_module, insert_point, msp):
    before = len(msp)
    block_module.add_to_drawing(msp)
    after = len(msp)

    new_entities = list(msp)[before:after]
    dx, dy = insert_point
    for e in new_entities:
        if hasattr(e.dxf, "insert"):
            pos = e.dxf.insert
            e.dxf.insert = (pos.x + dx, pos.y + dy)
        elif hasattr(e.dxf, "start") and hasattr(e.dxf, "end"):
            e.dxf.start = (e.dxf.start.x + dx, e.dxf.start.y + dy)
            e.dxf.end = (e.dxf.end.x + dx, e.dxf.end.y + dy)
        elif hasattr(e.dxf, "center"):
            center = e.dxf.center
            e.dxf.center = (center.x + dx, center.y + dy)


def build_drawing_from_csv(csv_path, output_path):
    doc = ezdxf.new()
    msp = doc.modelspace()

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw_name = row["block_name"].strip()
            block_name = sanitize_name(raw_name)
            x = float(row["position X1(src_position_x)"])
            y = float(row["position Y1(src_position_y)"])

            try:
                module_path = f"component_lib.block10.{block_name}"
                block_module = importlib.import_module(module_path)
                print(f"Chèn '{block_name}' tại ({x}, {y})")
                run_block_module_with_offset(block_module, (x, y), msp)
                print(f"Đã chèn block: {block_name}")
            except ModuleNotFoundError:
                print(f"Không tìm thấy block: {block_name}")
            except AttributeError:
                print(f"Block '{block_name}' không có hàm add_to_drawing(msp)")

    doc.saveas(output_path)
    print(f"\n🎉 Đã tạo bản vẽ: {output_path}")


if __name__ == "__main__":
    csv_path = r"E:\pythonProject\pythonProject1\test_picture\component.csv"
    output_path = r"E:\pythonProject\pythonProject1\test_picture\final_layout2.dxf"

    build_drawing_from_csv(csv_path, output_path)
