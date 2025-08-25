from dataclasses import dataclass
import numpy as np
from .base import Entity
from typing import Dict, Any

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
