import os
import pandas as pd
import numpy as np
from .json_loader import load_from_json
from .block_utils import parse_height_from_name, register_block_from_object
from ..transforms.matrix import rotation, scaling, translation

def load_from_excel(excel_path, base_dir, doc, msp):
    df = pd.read_excel(excel_path)
    parents = {}
    current_parent = None
    pole_x, pole_y, pole_height = None, None, None

    for _, row in df.iterrows():
        stt_raw = row["STT"]
        if pd.isna(stt_raw):
            stt = ""
        else:
            stt = str(stt_raw).strip()
            if stt.endswith(".0"):
                stt = stt[:-2]

        item_type = str(row["item_type"]).strip()
        name = str(row["item_name"]).strip()
        note_name = str(row["note"]).strip() if "note" in row and not pd.isna(row["note"]) else name
        layer_name = str(row["layer"]).strip() if "layer" in row and not pd.isna(row["layer"]) else "0"

        json_path = os.path.join(base_dir, item_type, f"{name}.json")
        if not os.path.exists(json_path):
            print(f"❌ Không tìm thấy file JSON cho {name} trong {item_type}")
            continue

        obj = load_from_json(json_path)

        rot = float(row["rotation_deg"]) if not pd.isna(row.get("rotation_deg")) else 0.0
        if rot != 0:
            obj.transform(rotation(rot))

        # --- CHA ---
        if "." not in stt:
            current_parent = stt
            parents[stt] = note_name

            pole_x = float(row["x( coordinates for pole and location extra block )"]) * 1000 if not pd.isna(row["x( coordinates for pole and location extra block )"]) else 0.0
            pole_y = float(row["y ( coordinates for pole and location for extra block )"]) * 1000 if not pd.isna(row["y ( coordinates for pole and location for extra block )"]) else 0.0

            pole_height = parse_height_from_name(name)
            if pole_height:
                xmin, ymin, xmax, ymax = obj.bounds()
                H = ymax - ymin
                if H > 0:
                    scale_factor = pole_height / H
                    obj.transform(scaling(scale_factor))

            xmin, ymin, xmax, ymax = obj.bounds()
            W = xmax - xmin
            H = ymax - ymin
            tx = pole_x - (xmin + W / 2)
            ty = pole_y - ymin
            obj.transform(translation(tx, ty))

            register_block_from_object(doc, note_name, obj)
            msp.add_blockref(note_name, (0, 0), dxfattribs={"layer": layer_name})
            print(f"✅ Chèn block CHA {note_name} (STT={stt}) tại ({pole_x},{pole_y}), H={pole_height}mm, layer={layer_name}")

        # --- CON ---
        else:
            parent_key = stt.split(".")[0]
            if parent_key in parents and pole_x is not None and pole_y is not None:
                at_val = float(row["y ( coordinates for pole and location for extra block )"]) * 1000 if not pd.isna(row["y ( coordinates for pole and location for extra block )"]) else 0.0

                x_offsets = []
                quantity = int(row["quantity"]) if not pd.isna(row.get("quantity")) else 1

                if quantity > 1:
                    if not pd.isna(row.get("x( coordinates for pole and location extra block )")):
                        try:
                            vals = [float(v.strip()) for v in str(row["x( coordinates for pole and location extra block )"]).split(",")]
                            x_offsets = [v * 1000.0 for v in vals]
                            print(f"ℹ️ Nhiều X nhập: {vals}m -> {x_offsets}mm")
                        except Exception:
                            x_offsets = [0.0] * quantity
                    else:
                        x_offsets = [0.0] * quantity
                else:
                    if pd.isna(row.get("x( coordinates for pole and location extra block )")):
                        x_offsets = [0.0]
                    else:
                        val_m = float(row["x( coordinates for pole and location extra block )"])
                        x_offsets = [val_m * 1000.0]
                        print(f"ℹ️ Đổi X {val_m}m -> {x_offsets[0]}mm")

                register_block_from_object(doc, note_name, obj)

                for lech_x in x_offsets:
                    tx = pole_x + lech_x
                    ty = pole_y + at_val
                    msp.add_blockref(note_name, (tx, ty), dxfattribs={"layer": layer_name})
                    print(f"   ➕ Gắn block CON {note_name} (STT={stt}) vào CHA {parent_key} tại ({tx},{ty}), AT={at_val}, X={lech_x}, layer={layer_name}")
            else:
                print(f"⚠️ Block {name} (STT={stt}) không có CHA hợp lệ!")
