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
        w = 0.6 * self.height * len(self.text)
        h = self.height
        x, y = self.insert
        return (x, y, x + w, y + h)


# --- Circle ---
@dataclass
class Circle(Entity):
    center: np.ndarray
    radius: float
    attribs: Dict[str, Any]

    def draw(self, msp):
        msp.add_circle((self.center[0], self.center[1]), self.radius, dxfattribs=self.attribs)

    def transform(self, matrix: np.ndarray):
        p = matrix @ np.array([self.center[0], self.center[1], 1.0])
        self.center = np.array([p[0], p[1]])
        sx = np.linalg.norm(matrix @ np.array([1, 0, 0]) - matrix @ np.array([0, 0, 0]))
        self.radius *= sx

    def bounds(self):
        x, y = self.center
        r = self.radius
        return (x-r, y-r, x+r, y+r)


# --- Arc ---
@dataclass
class Arc(Entity):
    center: np.ndarray
    radius: float
    start_angle: float
    end_angle: float
    attribs: Dict[str, Any]

    def draw(self, msp):
        msp.add_arc((self.center[0], self.center[1]), self.radius,
                    self.start_angle, self.end_angle,
                    dxfattribs=self.attribs)

    def transform(self, matrix: np.ndarray):
        p = matrix @ np.array([self.center[0], self.center[1], 1.0])
        self.center = np.array([p[0], p[1]])
        sx = np.linalg.norm(matrix @ np.array([1, 0, 0]) - matrix @ np.array([0, 0, 0]))
        self.radius *= sx

    def bounds(self):
        x, y = self.center
        r = self.radius
        return (x-r, y-r, x+r, y+r)


# --- Polyline ---
@dataclass
class Polyline(Entity):
    points: np.ndarray
    closed: bool
    attribs: Dict[str, Any]

    def draw(self, msp):
        msp.add_lwpolyline(self.points.tolist(),
                           dxfattribs=self.attribs,
                           close=self.closed)

    def transform(self, matrix: np.ndarray):
        new_pts = []
        for (x, y) in self.points:
            p = matrix @ np.array([x, y, 1.0])
            new_pts.append([p[0], p[1]])
        self.points = np.array(new_pts)

    def bounds(self):
        xs = self.points[:,0]
        ys = self.points[:,1]
        return (xs.min(), ys.min(), xs.max(), ys.max())


# --- Ellipse ---
@dataclass
class Ellipse(Entity):
    center: np.ndarray
    major_axis: np.ndarray
    ratio: float
    start_param: float
    end_param: float
    attribs: Dict[str, Any]

    def draw(self, msp):
        msp.add_ellipse(center=(self.center[0], self.center[1]),
                        major_axis=(self.major_axis[0], self.major_axis[1]),
                        ratio=self.ratio,
                        start_param=self.start_param,
                        end_param=self.end_param,
                        dxfattribs=self.attribs)

    def transform(self, matrix: np.ndarray):
        c = matrix @ np.array([self.center[0], self.center[1], 1.0])
        self.center = np.array([c[0], c[1]])
        ax = matrix @ np.array([self.major_axis[0], self.major_axis[1], 0.0])
        self.major_axis = np.array([ax[0], ax[1]])
        # ratio, start_param, end_param giữ nguyên tạm

    def bounds(self):
        x, y = self.center
        ax, ay = self.major_axis
        r = math.hypot(ax, ay)
        return (x-r, y-r, x+r, y+r)


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


def load_from_json(json_path: str) -> DrawingObject:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Nếu file JSON lưu ở dạng {"entities": [...]} thì lấy bên trong
    if isinstance(data, dict) and "entities" in data:
        entities_data = data["entities"]
    else:
        entities_data = data

    entities: List[Entity] = []
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
                # Ưu tiên fit_points, fallback sang control_points
                if "fit_points" in ent:
                    pts = [np.array(p, dtype=float) for p in ent["fit_points"]]
                elif "control_points" in ent:
                    pts = [np.array(p, dtype=float) for p in ent["control_points"]]
                else:
                    print(f"⚠️ SPLINE thiếu dữ liệu trong {os.path.basename(json_path)}")
                    continue

                # Nối spline thành polyline
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

# --- Parse height từ tên cột ---
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


def register_block_from_object(doc, block_name: str, obj: DrawingObject):
    """
    Đăng ký một block mới trong DXF document từ DrawingObject.
    Nếu block đã tồn tại thì xóa và tạo lại.
    """
    if block_name in doc.blocks:
        doc.blocks.delete_block(block_name, safe=False)
        # safe=False cho phép xóa cả khi block đang được tham chiếu

    block = doc.blocks.new(name=block_name)
    obj.draw(block)   # vẽ toàn bộ entity vào block
    return block



# --- Load Excel ---
def load_from_excel(excel_path, base_dir, doc, msp):
    df = pd.read_excel(excel_path)
    parents = {}
    current_parent = None
    pole_x, pole_y, pole_height = None, None, None

    for _, row in df.iterrows():
        # --- STT ---
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
        layer_name = str(row["layer"]).strip() if "layer" in row and not pd.isna(row["layer"]) else "0"  # ✅ layer

        json_path = os.path.join(base_dir, item_type, f"{name}.json")
        if not os.path.exists(json_path):
            print(f"❌ Không tìm thấy file JSON cho {name} trong {item_type}")
            continue

        obj = load_from_json(json_path)

        # --- rotation ---
        rot = float(row["rotation_deg"]) if not pd.isna(row.get("rotation_deg")) else 0.0
        if rot != 0:
            obj.transform(rotation(rot))

        # ---------------- CHA ----------------
        if "." not in stt:
            current_parent = stt
            parents[stt] = note_name

            pole_x = float(row["x( coordinates for pole and location extra block )"]) * 1000 if not pd.isna(row["x( coordinates for pole and location extra block )"]) else 0.0
            pole_y = float(row["y ( coordinates for pole and location for extra block )"]) * 1000 if not pd.isna(row["y ( coordinates for pole and location for extra block )"]) else 0.0

            # scale theo chiều cao cột (giữ nguyên code cũ)
            pole_height = parse_height_from_name(name)
            if pole_height:
                xmin, ymin, xmax, ymax = obj.bounds()
                H = ymax - ymin
                if H > 0:
                    scale_factor = pole_height / H
                    obj.transform(scaling(scale_factor))

            # align chân cột về (pole_x, pole_y)
            xmin, ymin, xmax, ymax = obj.bounds()
            W = xmax - xmin
            H = ymax - ymin
            tx = pole_x - (xmin + W / 2)
            ty = pole_y - ymin
            obj.transform(translation(tx, ty))

            # tạo block từ note_name
            register_block_from_object(doc, note_name, obj)
            msp.add_blockref(note_name, (0, 0), dxfattribs={"layer": layer_name})  # ✅ thêm layer
            print(f"✅ Chèn block CHA {note_name} (STT={stt}) tại ({pole_x},{pole_y}), H={pole_height}mm, layer={layer_name}")

        # ---------------- CON ----------------
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

                # chỉ tạo block 1 lần
                register_block_from_object(doc, note_name, obj)

                for lech_x in x_offsets:
                    tx = pole_x + lech_x
                    ty = pole_y + at_val
                    msp.add_blockref(note_name, (tx, ty), dxfattribs={"layer": layer_name})  # ✅ thêm layer
                    print(f"   ➕ Gắn block CON {note_name} (STT={stt}) vào CHA {parent_key} tại ({tx},{ty}), AT={at_val}, X={lech_x}, layer={layer_name}")
            else:
                print(f"⚠️ Block {name} (STT={stt}) không có CHA hợp lệ!")


# --- Vẽ hệ trục ---
def draw_axis_grid(msp, size=1000, step=100, show_axis=False, show_labels=False):
    if show_axis:
        msp.add_line((0, 0), (size, 0), dxfattribs={"color": 1})
        msp.add_line((0, 0), (0, size), dxfattribs={"color": 3})
    for x in range(0, size+1, step):
        msp.add_line((x, -10), (x, 10), dxfattribs={"color": 8})
    for y in range(0, size+1, step):
        msp.add_line((-10, y), (10, y), dxfattribs={"color": 8})


# --- Main ---
if __name__ == "__main__":
    base_dir = r"E:\pythonProject\pythonProject1\test_picture\lib_component\kind_of_block"
    excel_file = "poles_blocks_example4.xlsx"

    doc = ezdxf.new(setup=True)
    msp = doc.modelspace()
    load_from_excel(excel_file, base_dir, doc, msp)   # chỉ gọi, không return

    draw_axis_grid(msp, size=20000, step=1000)
    doc.saveas("poles_from_excel8.dxf")
    print("✅ Xuất DXF thành công từ Excel + JSON!")

