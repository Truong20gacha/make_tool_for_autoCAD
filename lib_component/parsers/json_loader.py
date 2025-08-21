import os, math, json
import numpy as np
from ..entities.line import Line
from ..entities.text import Text
from ..entities.circle import Circle
from ..entities.arc import Arc
from ..entities.polyline import Polyline
from ..entities.ellipse import Ellipse
from ..entities.drawing_object import DrawingObject

def load_from_json(json_path: str) -> DrawingObject:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Nếu file JSON lưu ở dạng {"entities": [...]} thì lấy bên trong
    if isinstance(data, dict) and "entities" in data:
        entities_data = data["entities"]
    else:
        entities_data = data

    entities = []
    for ent in entities_data:
        if ent is None or not isinstance(ent, dict):   # 🛠️ Fix lỗi NoneType
            continue

        typ = ent.get("type", "").upper()

        try:
            if typ == "LINE" and "pointsd" in ent:
                pts = np.array(ent["pointsd"], dtype=float)
                entities.append(Line(points=pts, attribs=ent.get("attribs", {})))

            elif typ == "TEXT":
                ins = np.array(ent.get("insert", [0.0, 0.0]), dtype=float)
                entities.append(Text(
                    text=ent.get("text", ""),
                    insert=ins,
                    height=float(ent.get("height", 250)),
                    attribs=ent.get("attribs", {})
                ))

            elif typ == "CIRCLE" and "center" in ent and "radius" in ent:
                entities.append(Circle(
                    center=np.array(ent["center"], dtype=float),
                    radius=float(ent["radius"]),
                    attribs=ent.get("attribs", {})
                ))

            elif typ == "ARC" and all(k in ent for k in ["center", "radius", "start_angle", "end_angle"]):
                entities.append(Arc(
                    center=np.array(ent["center"], dtype=float),
                    radius=float(ent["radius"]),
                    start_angle=float(ent["start_angle"]),
                    end_angle=float(ent["end_angle"]),
                    attribs=ent.get("attribs", {})
                ))

            elif typ in ("POLYLINE", "LWPOLYLINE") and "pointsd" in ent:
                pts = np.array(ent["pointsd"], dtype=float)
                entities.append(Polyline(
                    points=pts,
                    closed=bool(ent.get("closed", False)),
                    attribs=ent.get("attribs", {})
                ))

            elif typ == "ELLIPSE" and all(k in ent for k in ["center", "major_axis", "ratio"]):
                entities.append(Ellipse(
                    center=np.array(ent["center"], dtype=float),
                    major_axis=np.array(ent["major_axis"], dtype=float),
                    ratio=float(ent.get("ratio", 1.0)),
                    start_param=float(ent.get("start_param", 0.0)),
                    end_param=float(ent.get("end_param", 2 * math.pi)),
                    attribs=ent.get("attribs", {})
                ))

            elif typ == "SPLINE":
                if "fit_points" in ent:
                    pts = [np.array(p, dtype=float) for p in ent["fit_points"]]
                elif "control_points" in ent:
                    pts = [np.array(p, dtype=float) for p in ent["control_points"]]
                else:
                    print(f"⚠️ SPLINE thiếu dữ liệu trong {os.path.basename(json_path)}")
                    continue

                for i in range(len(pts) - 1):
                    entities.append(Line(
                        points=np.array([pts[i], pts[i + 1]]),
                        attribs=ent.get("attribs", {})
                    ))
                print(f"ℹ️ Chuyển SPLINE thành polyline gồm {len(pts)-1} đoạn trong {os.path.basename(json_path)}")

            else:
                print(f"⚠️ Bỏ qua entity {typ} trong {os.path.basename(json_path)} (thiếu dữ liệu)")

        except Exception as e:
            print(f"⚠️ Lỗi khi đọc entity {typ} trong {os.path.basename(json_path)}: {e}")

    return DrawingObject(entities=entities)
