import ezdxf
from lib_component.parsers.excel_loader import load_from_excel
from lib_component.utils.axis_debug import draw_axis_grid

if __name__ == "__main__":
    base_dir = r"E:\pythonProject\pythonProject1\test_picture\lib_component\kind_of_block"
    excel_file = "poles_blocks_example.xlsx"

    doc = ezdxf.new()
    msp = doc.modelspace()

    all_objs = load_from_excel(excel_file, base_dir)
    for obj in all_objs:
        obj.draw(msp)

    draw_axis_grid(msp, size=20000, step=1000)
    doc.saveas("poles_from_excel.dxf")
    print("✅ Xuất DXF thành công từ Excel + JSON!")
