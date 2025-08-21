import re

def parse_height_from_name(name: str) -> float:
    """
    Lấy số đầu tiên trong tên (ví dụ: cot_PC_17_230_14 -> 17m -> 17000mm)
    """
    if not isinstance(name, str):
        return None
    m = re.search(r"(\d+)", name)
    if m:
        val_m = float(m.group(1))
        return val_m * 1000.0
    return None


def register_block_from_object(doc, block_name: str, obj):
    """
    Đăng ký một block mới trong DXF document từ DrawingObject.
    Nếu block đã tồn tại thì xóa và tạo lại.
    """
    if block_name in doc.blocks:
        doc.blocks.delete_block(block_name, safe=False)

    block = doc.blocks.new(name=block_name)
    obj.draw(block)   # vẽ toàn bộ entity vào block
    return block
