import os
import numpy as np

def build_anchor_mapping_from_sheet1(df1, base_dir, load_from_json=None, AnchorClass=None):
    """
    Tạo mapping: (id_manh, x_offset, anchor_name, y_val) -> anchor_local
    - df1: DataFrame Sheet1 (block mảnh)
    - base_dir: thư mục chứa block json
    - load_from_json: hàm load block json ra object (phải truyền vào nếu nằm module ngoài)
    - AnchorClass: class Anchor (phải truyền vào nếu dùng outside)
    """
    mapping = {}
    for idx, row in df1.iterrows():
        stt = str(row["STT"]).strip()
        if not stt or "." not in stt:
            continue
        id_manh = stt.replace(".0", "")

        # Xử lý offset X
        try:
            x_offsets = [float(x.strip()) * 1000 for x in str(row.get("x( coordinates for pole and location extra block )", "0")).split(",")]
        except Exception:
            x_offsets = [0.0]
        y_val = float(row.get("y ( coordinates for pole and location for extra block )", 0)) * 1000

        item_type = str(row["item_type"]).strip()
        item_name = str(row["item_name"]).strip()
        json_path = os.path.join(base_dir, item_type, f"{item_name}.json")
        if not os.path.exists(json_path):
            continue

        # Load block object
        obj = load_from_json(json_path)
        for ent in obj.entities:
            # Có thể dùng isinstance hoặc kiểm tra bằng attr nếu truyền vào class ngoài
            if (AnchorClass and isinstance(ent, AnchorClass)) or (not AnchorClass and getattr(ent, 'tag', None) is not None):
                anchor_name = ent.tag
                anchor_local = tuple(ent.insert)
                for xi in x_offsets:
                    key = (id_manh, xi, anchor_name, y_val)
                    mapping[key] = anchor_local
    return mapping

def lookup_y_from_sheet1(df1, id_manh, vi_tri):
    """
    Tra cứu y_val trong Sheet1 (block mảnh) từ id_manh & vi_tri (theo đơn vị m)
    """
    for _, row in df1.iterrows():
        stt = str(row["STT"]).strip()
        if stt.endswith(".0"): stt = stt[:-2]
        if stt == id_manh:
            x_str = str(row["x( coordinates for pole and location extra block )"])
            x_vals = [float(x.strip()) for x in x_str.split(",") if x.strip() != ""]
            if any(abs(xi - vi_tri) < 1e-6 for xi in x_vals):
                try:
                    return float(row["y ( coordinates for pole and location for extra block )"]) * 1000
                except Exception:
                    return None
    print(f"[DEBUG] Không tìm thấy CON={id_manh}, vi_tri={vi_tri} trong Sheet1")
    return None

def draw_wires_from_sheet2(df1, df2, anchor_mapping, pole_position_mapping, msp):
    """
    Vẽ dây điện giữa các block theo thông tin trong sheet2 (df2).
    Chỉ dùng các thông tin cần thiết, không tự ý thêm label hoặc block name ra ngoài.
    """
    for idx, row in df2.iterrows():
        id_from_full = str(row["ID_manh_from"])
        id_to_full = str(row["ID_manh_to"])
        # Chỉ lấy phần con cuối (vd 1.1.7 -> 1.7)
        id_from = ".".join(id_from_full.split(".")[-2:]) if id_from_full.count(".") >= 2 else id_from_full
        id_to   = ".".join(id_to_full.split(".")[-2:]) if id_to_full.count(".") >= 2 else id_to_full

        vi_tri_from = float(row["vi_tri_manh_from"]) * 1000
        vi_tri_to   = float(row["vi_tri_manh_to"]) * 1000
        anchor_from = str(row["anchor_from"]).strip()
        anchor_to   = str(row["anchor_to"]).strip()
        block_name  = str(row["cable_type and note"]).strip()   # LẤY ĐÚNG TỪ CỘT CUỐI

        y_from = lookup_y_from_sheet1(df1, id_from, vi_tri_from / 1000)
        y_to   = lookup_y_from_sheet1(df1, id_to, vi_tri_to / 1000)

        key1 = (id_from, vi_tri_from, anchor_from, y_from)
        key2 = (id_to,   vi_tri_to,   anchor_to,   y_to)

        anchor_local_from = anchor_mapping.get(key1)
        anchor_local_to = anchor_mapping.get(key2)

        pole_x_from, pole_y_from = pole_position_mapping.get(id_from, (0,0))
        pole_x_to, pole_y_to = pole_position_mapping.get(id_to, (0,0))

        if anchor_local_from is not None:
            p1 = (pole_x_from + vi_tri_from + anchor_local_from[0],
                  pole_y_from + y_from + anchor_local_from[1])
        else:
            p1 = None

        if anchor_local_to is not None:
            p2 = (pole_x_to + vi_tri_to + anchor_local_to[0],
                  pole_y_to + y_to + anchor_local_to[1])
        else:
            p2 = None

        print(f"[QUERY] {key1} -> {p1}")
        print(f"[QUERY] {key2} -> {p2}")

        if p1 is None or p2 is None:
            print(f"❌ Không tìm thấy anchor: CHA={id_from_full} ({id_from}) Anchor={anchor_from} "
                  f"hoặc CHA={id_to_full} ({id_to}) Anchor={anchor_to}")
            continue

        if block_name in msp.doc.blocks:
            msp.add_blockref(block_name, p1)
            print(f"✅ Insert block dây '{block_name}' tại {p1}")
        else:
            # --- Vẽ dây võng mềm mại ---
            d = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) ** 0.5
            depth = min(max(d / 8, 300), 2500)
            pts = wire_vong(p1, p2, n=24, depth=depth)
            msp.add_lwpolyline(pts, dxfattribs={"layer": "CABLE", "color": 1})

            print(f"✅ Vẽ dây võng từ {id_from_full} ({id_from}) [{anchor_from}] {p1} → "
                  f"{id_to_full} ({id_to}) [{anchor_to}] {p2}, tên dây {block_name}")


def wire_vong(p1, p2, n=20, depth=800):
    """
    Sinh ra các điểm (list [x, y]) cho dây võng mềm (parabol)
    """
    xs = np.linspace(p1[0], p2[0], n)
    ys = []
    for i, x in enumerate(xs):
        t = i / (n - 1)
        y = (1 - t) * p1[1] + t * p2[1]
        offset = -4 * depth * t * (1 - t)
        ys.append(y + offset)
    return [[x, y] for x, y in zip(xs, ys)]
