import json
import ezdxf

def load_from_json(json_path: str):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def draw_block(msp, block_data, insert=(0, 0), scale=1.0, layer="0"):
    for ent in block_data.get("entities", []):
        t = ent.get("type")
        if t == "LINE":
            (x1, y1, x2, y2) = ent["pointsd"]
            msp.add_line(
                (x1 * scale + insert[0], y1 * scale + insert[1]),
                (x2 * scale + insert[0], y2 * scale + insert[1]),
                dxfattribs={"layer": layer},
            )
        elif t == "TEXT":
            ins = ent["insert"]
            msp.add_text(
                ent["text"],
                dxfattribs={
                    "insert": (ins[0] * scale + insert[0], ins[1] * scale + insert[1]),
                    "height": ent["height"] * scale,
                    "layer": layer,
                },
            )
    # TODO: mở rộng thêm CIRCLE, ARC, ...
