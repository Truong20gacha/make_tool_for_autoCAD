import ezdxf
import pandas as pd
from lib_component.parsers.excel_loader import load_from_excel
from lib_component.parsers.wire_utils import (
    build_anchor_mapping_from_sheet1,
    lookup_y_from_sheet1,
    draw_wires_from_sheet2,
)
from lib_component.utils.axis_debug import draw_axis_grid

def build_pole_position_mapping(df1):
    """
    Trả về dict: id_con (VD: '1.7') -> (pole_x, pole_y) thực tế của cột CHA
    """
    mapping = {}
    current_cha = None
    pole_x = None
    pole_y = None
    for _, row in df1.iterrows():
        stt_raw = str(row['STT']).strip()
        if stt_raw.endswith('.0'): stt_raw = stt_raw[:-2]
        if '.' not in stt_raw:  # CHA
            current_cha = stt_raw
            pole_x = float(row["x( coordinates for pole and location extra block )"]) * 1000 if not pd.isna(row["x( coordinates for pole and location extra block )"]) else 0.0
            pole_y = float(row["y ( coordinates for pole and location for extra block )"]) * 1000 if not pd.isna(row["y ( coordinates for pole and location for extra block )"]) else 0.0
        else:
            id_con = stt_raw  # ví dụ: '1.7'
            mapping[id_con] = (pole_x, pole_y)
    return mapping

def main():
    # --- Config đường dẫn ---
    base_dir = r"E:\pythonProject\pythonProject1\test_picture\lib_component\kind_of_block"
    excel_file = "poles_blocks_example6.xlsx"

    # --- Đọc 2 sheet Excel ---
    df1 = pd.read_excel(excel_file, sheet_name="Sheet1")   # Block/mảnh
    df2 = pd.read_excel(excel_file, sheet_name="Sheet2")   # Nối dây

    # --- Khởi tạo file DXF ---
    doc = ezdxf.new(setup=True)
    msp = doc.modelspace()

    # --- Vẽ block cột/mảnh từ Sheet1 ---
    load_from_excel(excel_file, base_dir, doc, msp)

    # --- Build mapping vị trí CHA/CON ---
    pole_position_mapping = build_pole_position_mapping(df1)

    # --- Build anchor mapping từ Sheet1 ---
    from lib_component.parsers.json_loader import load_from_json
    from lib_component.entities.anchor import Anchor
    anchor_mapping = build_anchor_mapping_from_sheet1(
        df1, base_dir, load_from_json=load_from_json, AnchorClass=Anchor
    )

    # --- Vẽ dây điện từ Sheet2 ---
    draw_wires_from_sheet2(
        df1, df2, anchor_mapping, pole_position_mapping, msp,
    )

    # --- Vẽ hệ trục debug ---
    draw_axis_grid(msp, size=20000, step=1000, show_axis=False, show_labels=False)

    # --- Lưu file DXF ---
    doc.saveas("poles_from_excel8_fullwire.dxf")
    print("✅ Xuất DXF hoàn chỉnh cả block + dây điện từ Excel + JSON!")

if __name__ == "__main__":
    main()
