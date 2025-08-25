import os, math, json
import numpy as np
from ..entities.line import Line
from ..entities.text import Text
from ..entities.circle import Circle
from ..entities.arc import Arc
from ..entities.polyline import Polyline
from ..entities.ellipse import Ellipse
from ..entities.drawing_object import DrawingObject
from ..entities.anchor import Anchor
from ..entities.blockref import BlockRef
from .. entities.leader import Leader
from ..entities.point import Point
from ..entities.mtext import MText
from ..entities.base import Entity

def load_from_json(json_path: str) -> DrawingObject:
    import os, math, numpy as np, json
    from typing import List

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict) and "entities" in data:
        entities_data = data["entities"]
    else:
        entities_data = data

    entities: List[Entity] = []

    for ent in entities_data:
        if ent is None or not isinstance(ent, dict):
            continue

        typ = ent.get("type", "").upper()

        try:
            # --- Các entity cũ ---
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


            elif typ == "ELLIPSE":

                center = ent.get("center")

                major_axis = ent.get("major_axis")

                ratio = ent.get("ratio")

                if center is not None and major_axis is not None and ratio is not None:

                    entities.append(Ellipse(

                        center=np.array(center, dtype=float),

                        major_axis=np.array(major_axis, dtype=float),

                        ratio=float(ratio),

                        start_param=float(ent.get("start_param", 0.0)),

                        end_param=float(ent.get("end_param", 2 * math.pi)),

                        attribs=ent.get("attribs", {})

                    ))

                else:

                    print(f"⚠️ [ELLIPSE thiếu dữ liệu fields] {ent} trong {os.path.basename(json_path)}")


            elif typ == "SPLINE":
                if "fit_points" in ent:
                    pts = [np.array(p, dtype=float) for p in ent["fit_points"]]
                elif "control_points" in ent:
                    pts = [np.array(p, dtype=float) for p in ent["control_points"]]
                else:
                    print(f"⚠️ [SPLINE thiếu dữ liệu] {os.path.basename(json_path)}")
                    continue

                for i in range(len(pts) - 1):
                    entities.append(Line(
                        points=np.array([pts[i], pts[i + 1]]),
                        attribs=ent.get("attribs", {})
                    ))
                print(f"ℹ️ [Chuyển SPLINE] thành polyline gồm {len(pts)-1} đoạn ({os.path.basename(json_path)})")

            # --- Các entity mới bổ sung ---
            elif typ == "MTEXT":
                ins = np.array(ent.get("insert", [0.0, 0.0]), dtype=float)
                # TODO: Định nghĩa class MText nếu chưa có
                entities.append(MText(
                    text=ent.get("text", ""),
                    insert=ins,
                    height=float(ent.get("height", 250)),
                    attribs=ent.get("attribs", {})
                ))

            elif typ == "LEADER" and "vertices" in ent:
                pts = np.array(ent["vertices"], dtype=float)
                # TODO: Định nghĩa class Leader nếu chưa có
                entities.append(Leader(
                    vertices=pts,
                    attribs=ent.get("attribs", {})
                ))

            elif typ == "POINT":
                location = np.array(ent.get("location", [0.0, 0.0]), dtype=float)
                # TODO: Định nghĩa class Point nếu chưa có
                entities.append(Point(
                    location=location,
                    attribs=ent.get("attribs", {})
                ))

            elif typ in ("BLOCKREF", "INSERT"):
                block_name = ent.get("block_name", "")
                insert = np.array(ent.get("insert", [0.0, 0.0]), dtype=float)
                scale = float(ent.get("scale", 1.0))
                rotation = float(ent.get("rotation", 0.0))
                # TODO: Định nghĩa class BlockRef nếu chưa có
                entities.append(BlockRef(
                    block_name=block_name,
                    insert=insert,
                    scale=scale,
                    rotation=rotation,
                    attribs=ent.get("attribs", {})
                ))

            # --- Thêm anchor ---
            elif typ == "ANCHOR":
                tag = ent.get("tag", "")
                insert = np.array(ent.get("insert", [0.0, 0.0]), dtype=float)
                entities.append(Anchor(tag=tag, insert=insert, attribs=ent.get("attribs", {})))

            else:
                print(f"⚠️ [Bỏ qua entity] {typ} trong {os.path.basename(json_path)} (thiếu dữ liệu)")

        except Exception as e:
            print(f"⚠️ [Lỗi đọc entity] {typ} trong {os.path.basename(json_path)}: {e}")

    return DrawingObject(entities=entities)
