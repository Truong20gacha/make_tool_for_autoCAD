import os
import pandas as pd

from .json_loader import load_from_json
from .mota_parser import parse_mota, parse_lechx
from ..transforms.matrix import translation, scaling, rotation
from ..entities.drawing_object import DrawingObject


def load_from_excel(xlsx_path: str, base_dir: str) -> list[DrawingObject]:
    df = pd.read_excel(xlsx_path, sheet_name="Sheet1")
    objs = []

    pole_x, pole_y, pole_height = None, None, None

    for _, row in df.iterrows():
        module = str(row["template_module"]).strip()
        name = str(row["name_of_template"]).strip()
        json_path = os.path.join(base_dir, module, f"{name}.json")

        if not os.path.exists(json_path):
            print(f"⚠️ Không tìm thấy file JSON cho {name}")
            continue

        obj = load_from_json(json_path)

        rot = float(row["rotation_deg"]) if not pd.isna(row.get("rotation_deg")) else 0
        if rot != 0:
            obj.transform(rotation(rot))

        if str(row["layer"]).upper() == "POLE":
            # Trụ chính
            # X (luôn coi là mét -> đổi sang mm)
            if not pd.isna(row["x"]):
                pole_x = float(row["x"]) * 1000
                print(f"ℹ️ Đổi X {row['x']}m -> {pole_x}mm")
            else:
                pole_x = 0.0

            # Y (luôn coi là mét -> đổi sang mm)
            if not pd.isna(row["y"]):
                pole_y = float(row["y"]) * 1000
                print(f"ℹ️ Đổi Y {row['y']}m -> {pole_y}mm")
            else:
                pole_y = 0.0

            # Height
            pole_height = float(row["height"]) if not pd.isna(row["height"]) else None
            if pole_height and pole_height < 1000:
                print(f"ℹ️ Đổi height {pole_height}m -> {pole_height*1000}mm")
                pole_height *= 1000.0

            # scale trụ theo height
            if pole_height:
                xmin, ymin, xmax, ymax = obj.bounds()
                H = ymax - ymin
                if H > 0:
                    scale_factor = pole_height / H
                    obj.transform(scaling(scale_factor))

            # Lấy lại bounds sau khi scale
            xmin, ymin, xmax, ymax = obj.bounds()
            W = xmax - xmin
            H = ymax - ymin

            # Tính dịch chuyển để chân cột về pole_y và tim cột về pole_x
            tx = pole_x - (xmin + W / 2)
            ty = pole_y - ymin
            obj.transform(translation(tx, ty))

            objs.append(obj)
            print(f"✅ Chèn trụ {name} tại ({pole_x},{pole_y}), H={pole_height}mm")

        else:
            # Block con: bám theo trụ
            if pole_x is None or pole_y is None:
                print(f"⚠️ Block {name} được khai báo trước khi có trụ chính!")
                continue

            # AT
            at_val = parse_mota(row.get("mo_ta", ""))

            # offset X: ưu tiên từ mo_ta, nếu không thì lấy từ cột x, nếu trống thì 0
            # offset X: ưu tiên từ mo_ta, nếu không thì lấy từ cột x
            lech_x = parse_lechx(row.get("mo_ta", ""))
            if lech_x == 0.0:
                if pd.isna(row.get("x")):
                    lech_x = 0.0
                else:
                    val_m = float(row["x"])
                    lech_x = val_m * 1000.0
                    print(f"ℹ️ Đổi X {val_m}m -> {lech_x}mm")

            tx = pole_x + lech_x
            ty = pole_y + at_val

            obj.transform(translation(tx, ty))
            objs.append(obj)
            print(f"✅ Chèn block {name} tại ({tx},{ty}), AT={at_val}, X={lech_x}")

    return objs