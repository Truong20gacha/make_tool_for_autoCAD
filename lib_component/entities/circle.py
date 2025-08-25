from dataclasses import dataclass
import numpy as np
from .base import Entity

@dataclass
class Circle(Entity):
    center: np.ndarray
    radius: float
    attribs: dict

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
