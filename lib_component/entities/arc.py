from dataclasses import dataclass
import numpy as np
from .base import Entity

@dataclass
class Arc(Entity):
    center: np.ndarray
    radius: float
    start_angle: float
    end_angle: float
    attribs: dict

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
