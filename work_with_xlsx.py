from dataclasses import dataclass
from typing import List, Dict, Any
import numpy as np
import json
import ezdxf
import math
import pandas as pd
import os
import re


# --- Base Entity ---
class Entity:
    def draw(self, msp):
        raise NotImplementedError

    def transform(self, matrix: np.ndarray):
        raise NotImplementedError

    def bounds(self):
        raise NotImplementedError


# --- Line ---
@dataclass
class Line(Entity):
    points: np.ndarray  # [x1, y1, x2, y2]
    attribs: Dict[str, Any]

    def draw(self, msp):
        (x1, y1, x2, y2) = self.points
        msp.add_line((x1, y1), (x2, y2), dxfattribs=self.attribs)

    def transform(self, matrix: np.ndarray):
        p1 = matrix @ np.array([self.points[0], self.points[1], 1.0])
        p2 = matrix @ np.array([self.points[2], self.points[3], 1.0])
        self.points = np.array([p1[0], p1[1], p2[0], p2[1]])

    def bounds(self):
        x1, y1, x2, y2 = self.points
        return (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))


# --- Text ---
@dataclass
class Text(Entity):
    text: str
    insert: np.ndarray
    height: float
    attribs: Dict[str, Any]

    def draw(self, msp):
        msp.add_text(self.text, dxfattribs={
            "insert": (self.insert[0], self.insert[1]),
            "height": self.height,
            **self.attribs
        })

    def transform(self, matrix: np.ndarray):
        p = matrix @ np.array([self.insert[0], self.insert[1], 1.0])
        self.insert = np.array([p[0], p[1]])
        # scale theo X để phóng chữ
        sx = np.linalg.norm(matrix @ np.array([1, 0, 0]) - matrix @ np.array([0, 0, 0]))
        self.height *= sx

    def bounds(self):
        # đơn giản ước lượng bbox text
        w = 0.6 * self.height * len(self.text)
        h = self.height
        x, y = self.insert
        return (x, y, x + w, y + h)


# --- DrawingObject ---
@dataclass
class DrawingObject:
    entities: List[Entity]

    def draw(self, msp):
        for ent in self.entities:
            ent.draw(msp)

    def transform(self, matrix: np.ndarray):
        for ent in self.entities:
            ent.transform(matrix)

    def bounds(self):
        if not self.entities:
            return (0, 0, 0, 0)
        bboxes = [ent.bounds() for ent in self.entities]
        xmin = min(b[0] for b in bboxes)
        ymin = min(b[1] for b in bboxes)
        xmax = max(b[2] for b in bboxes)
        ymax = max(b[3] for b in bboxes)
        return (xmin, ymin, xmax, ymax)


# --- Ma trận transform ---
def translation(tx, ty):
    return np.array([[1, 0, tx],
                     [0, 1, ty],
                     [0, 0, 1]])


def scaling(s):
    return np.array([[s, 0, 0],
                     [0, s, 0],
                     [0, 0, 1]])


def rotation(angle_deg):
    rad = math.radians(angle_deg)
    c, s = math.cos(rad), math.sin(rad)
    return np.array([[c, -s, 0],
                     [s,  c, 0],
                     [0,  0, 1]])


# --- Load JSON ---
def load_from_json(json_path: str) -> DrawingObject:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict) and "entities" in data:
        entities_data = data["entities"]
    else:
        entities_data = data

    entities: List[Entity] = []
    for ent in entities_data:
        if ent["type"] == "LINE":
            pts = np.array(ent["pointsd"], dtype=float)
            entities.append(Line(points=pts, attribs=ent["attribs"]))
        elif ent["type"] == "TEXT":
            ins = np.array(ent["insert"], dtype=float)
            entities.append(Text(text=ent["text"], insert=ins,
                                 height=ent["height"], attribs=ent["attribs"]))
    return DrawingObject(entities=entities)


# --- Parse mo_ta để lấy AT ---
def parse_mota(mo_ta: str) -> float:
    if not isinstance(mo_ta, str):
        return 0.0
    match = re.search(r"AT\s*=\s*([0-9.+-]+)", mo_ta)
    if match:
        at_val = float(match.group(1))
        # nếu AT < 1000 thì hiểu là mét -> đổi sang mm
        if abs(at_val) < 1000:
            print(f"ℹ️ Đổi AT {at_val}m -> {at_val*1000}mm")
            at_val *= 1000.0
        return at_val
    return 0.0


def parse_lechx(mo_ta: str) -> float:
    if not isinstance(mo_ta, str):
        return 0.0
    match = re.search(r"X\s*=\s*([0-9.+-]+)", mo_ta)
    if match:
        val_m = float(match.group(1))   # luôn hiểu đơn vị là mét
        val_mm = val_m * 1000.0         # đổi sang mm
        print(f"ℹ️ Đổi X {val_m}m -> {val_mm}mm")
        return val_mm
    return 0.0




# --- Load Excel ---
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


# --- Vẽ hệ trục XY để debug ---
def draw_axis_grid(msp, size: int = 1000, step: int = 100):
    msp.add_line((0, 0), (size, 0), dxfattribs={"color": 1})
    msp.add_line((0, 0), (0, size), dxfattribs={"color": 3})

    for x in range(0, size + 1, step):
        msp.add_line((x, -10), (x, 10), dxfattribs={"color": 8})
        txt = msp.add_text(str(x), dxfattribs={"height": 20, "color": 8})
        txt.set_dxf_attrib("insert", (x, -40))

    for y in range(0, size + 1, step):
        msp.add_line((-10, y), (10, y), dxfattribs={"color": 8})
        txt = msp.add_text(str(y), dxfattribs={"height": 20, "color": 8})
        txt.set_dxf_attrib("insert", (-60, y - 10))

    msp.add_circle((0, 0), 15, dxfattribs={"color": 7})
    txt_o = msp.add_text("O", dxfattribs={"height": 25, "color": 7})
    txt_o.set_dxf_attrib("insert", (-30, -30))


# --- Main ---
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
