import json
import numpy as np
import os
from ..entities.line import Line
from ..entities.text import Text
from ..entities.drawing_object import DrawingObject



def load_from_json(json_path: str) -> DrawingObject:
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Không tìm thấy {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    entities_data = data["entities"] if "entities" in data else data
    entities = []

    for ent in entities_data:
        if ent["type"] == "LINE":
            pts = np.array(ent["pointsd"], dtype=float)
            entities.append(Line(points=pts, attribs=ent["attribs"]))
        elif ent["type"] == "TEXT":
            ins = np.array(ent["insert"], dtype=float)
            entities.append(Text(text=ent["text"], insert=ins,
                                 height=ent["height"], attribs=ent["attribs"]))
    return DrawingObject(entities=entities)
