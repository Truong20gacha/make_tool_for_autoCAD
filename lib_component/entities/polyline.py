from dataclasses import dataclass
import numpy as np
from .base import Entity

@dataclass
class Polyline(Entity):
    points: np.ndarray
    closed: bool
    attribs: dict

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
