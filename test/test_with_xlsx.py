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

@dataclass
class MText:
    text: str
    insert: np.ndarray  # [x, y]
    height: float
    attribs: Dict[str, Any]

    def draw(self, msp):
        # Giả sử msp là modelspace của ezdxf
        msp.add_mtext(self.text, dxfattribs=self.attribs).set_location(tuple(self.insert))

@dataclass
class Leader:
    vertices: np.ndarray  # [[x1, y1], [x2, y2], ...]
    attribs: Dict[str, Any]

    def draw(self, msp):
        # Tùy thư viện, có thể cần custom cho leader trong ezdxf
        msp.add_lwpolyline([tuple(pt) for pt in self.vertices], dxfattribs=self.attribs)

@dataclass
class Point:
    location: np.ndarray  # [x, y]
    attribs: Dict[str, Any]

    def draw(self, msp):
        msp.add_point(tuple(self.location), dxfattribs=self.attribs)

@dataclass
class BlockRef:
    block_name: str
    insert: np.ndarray  # [x, y]
    scale: float
    rotation: float
    attribs: Dict[str, Any]

    def draw(self, msp):
        # Block insert: tùy theo cách bạn register block và context của ezdxf
        msp.add_blockref(self.block_name, tuple(self.insert),
                         dxfattribs=self.attribs).transform(scale=(self.scale, self.scale, 1), rotation=self.rotation)
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
            if isinstance(ent, Anchor):
                # DEBUG: Vẽ Anchor bằng circle nhỏ, layer ANCHOR
                msp.add_circle((ent.insert[0], ent.insert[1]), 20, dxfattribs={"color": 1, "layer": "ANCHOR"})
            else:
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

@dataclass
class Anchor:
    tag: str
    insert: np.ndarray
    attribs: Dict

    def transform(self, matrix: np.ndarray):
        p = matrix @ np.array([self.insert[0], self.insert[1], 1.0])
        self.insert = np.array([p[0], p[1]])


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
    block_con_dict = {}

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
        layer_name = str(row["layer"]).strip() if "layer" in row and not pd.isna(row["layer"]) else "0"

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
        if "." not in stt:   # Gặp số nguyên, đổi CHA
            current_parent = stt
            parents[current_parent] = note_name

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

            # --- align block dựa trên anchor (nếu có) ---
            anchor_entity = None
            for ent in obj.entities:
                if isinstance(ent, Anchor):
                    anchor_entity = ent
                    break

            if anchor_entity is not None:
                ax, ay = anchor_entity.insert
                tx = pole_x - ax
                ty = pole_y - ay
                obj.transform(translation(tx, ty))
                print(f"ℹ️ Đặt block CHA align theo anchor ({ax}, {ay}) về ({pole_x}, {pole_y})")
            else:
                xmin, ymin, xmax, ymax = obj.bounds()
                W = xmax - xmin
                H = ymax - ymin
                tx = pole_x - (xmin + W / 2)
                ty = pole_y - ymin
                obj.transform(translation(tx, ty))

            register_block_from_object(doc, note_name, obj)
            msp.add_blockref(note_name, (0, 0), dxfattribs={"layer": layer_name})
            print(f"✅ Chèn block CHA {note_name} (STT={stt}) tại ({pole_x},{pole_y}), H={pole_height}mm, layer={layer_name}")

        # ---------------- CON ----------------
        else:
            parent_key = current_parent
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

                # Lưu thông tin block CON vào dict cho mapping anchor
                id_manh = stt
                for lech_x in x_offsets:
                    # (id_manh, x, y, note_name) -> obj
                    block_con_dict[(id_manh, lech_x, at_val, note_name)] = obj

                    tx = pole_x + lech_x
                    ty = pole_y + at_val
                    msp.add_blockref(note_name, (tx, ty), dxfattribs={"layer": layer_name})
                    print(f"   ➕ Gắn block CON {note_name} (STT={stt}) vào CHA {parent_key} tại ({tx},{ty}), AT={at_val}, X={lech_x}, layer={layer_name}")
            else:
                print(f"⚠️ Block {name} (STT={stt}) không có CHA hợp lệ!")

    # TRẢ RA dict để build anchor mapping
    return block_con_dict


def split_cha_con_from_id_manh(id_manh):
    parts = str(id_manh).split(".")
    if len(parts) >= 2:
        cha = parts[0]
        con = ".".join(parts[1:])
        return cha, con
    else:
        return id_manh, None


import os
import json

def build_pole_position_mapping(df1):
    """
    Trả về dict: id_con (VD: '1.7') -> (pole_x, pole_y) thực tế của cột CHA
    """
    mapping = {}
    current_cha = None
    pole_x = None
    pole_y = None
    for _, row in df1.iterrows():
        stt_raw = str(row['STT']).strip()
        if stt_raw.endswith('.0'): stt_raw = stt_raw[:-2]
        if '.' not in stt_raw:  # CHA
            current_cha = stt_raw
            pole_x = float(row["x( coordinates for pole and location extra block )"]) * 1000 if not pd.isna(row["x( coordinates for pole and location extra block )"]) else 0.0
            pole_y = float(row["y ( coordinates for pole and location for extra block )"]) * 1000 if not pd.isna(row["y ( coordinates for pole and location for extra block )"]) else 0.0
        else:
            id_con = stt_raw  # ví dụ: '1.7'
            mapping[id_con] = (pole_x, pole_y)
    return mapping

import numpy as np

def wire_vong(p1, p2, n=20, depth=800):
    """
    Sinh ra các điểm (list [x, y]) cho dây võng mềm (parabol),
    n: số điểm (mịn hơn nếu n lớn), depth: độ võng xuống (âm = võng xuống).
    """
    xs = np.linspace(p1[0], p2[0], n)
    ys = []
    for i, x in enumerate(xs):
        t = i / (n - 1)
        y = (1 - t) * p1[1] + t * p2[1]
        offset = -4 * depth * t * (1 - t)
        ys.append(y + offset)
    return [[x, y] for x, y in zip(xs, ys)]


def build_anchor_mapping_from_sheet1(df1, base_dir):
    mapping = {}
    for idx, row in df1.iterrows():
        stt = str(row["STT"]).strip()
        if pd.isna(stt) or "." not in stt:
            continue
        id_manh = stt.replace(".0", "")

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

        obj = load_from_json(json_path)
        for ent in obj.entities:
            if isinstance(ent, Anchor):
                anchor_name = ent.tag
                anchor_local = tuple(ent.insert)
                for xi in x_offsets:
                    key = (id_manh, xi, anchor_name, y_val)
                    mapping[key] = anchor_local
    return mapping

def lookup_y_from_sheet1(df1, id_manh, vi_tri):
    # id_manh là CON (vd: '1.7')
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
    for idx, row in df2.iterrows():
        id_from_full = str(row["ID_manh_from"])
        id_to_full = str(row["ID_manh_to"])
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
    excel_file = "poles_blocks_example6.xlsx"

    doc = ezdxf.new(setup=True)
    msp = doc.modelspace()


    # Đọc 2 sheet chỉ 1 lần, dùng suốt code
    df1 = pd.read_excel(excel_file, sheet_name="Sheet1")   # block mảnh
    df2 = pd.read_excel(excel_file, sheet_name="Sheet2")   # nối dây

    # VẼ BLOCK CỘT/MẢNH
    load_from_excel(excel_file, base_dir, doc, msp)

    # Tạo mapping vị trí CHA cho từng CON
    pole_position_mapping = build_pole_position_mapping(df1)
    anchor_mapping = build_anchor_mapping_from_sheet1(df1, base_dir)

    draw_wires_from_sheet2(df1, df2, anchor_mapping, pole_position_mapping, msp)

    draw_axis_grid(msp, size=20000, step=1000)
    doc.saveas("test_co_anchor_with_wire3.dxf")
    print("✅ Xuất DXF hoàn chỉnh cả dây điện từ Excel + JSON!")



