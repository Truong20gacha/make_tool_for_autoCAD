from dataclasses import dataclass
import numpy as np
import math
from .base import Entity

@dataclass
class Ellipse(Entity):
    center: np.ndarray
    major_axis: np.ndarray
    ratio: float
    start_param: float
    end_param: float
    attribs: dict

    def draw(self, msp):
        msp.add_ellipse(center=(self.center[0], self.center[1]),
                        major_axis=(self.major_axis[0], self.major_axis[1]),
                        ratio=self.ratio,
                        start_param=self.start_param,
                        end_param=self.end_param,
                        dxfattribs=self.attribs)

    def transform(self, matrix):
        c = matrix @ np.array([self.center[0], self.center[1], 1.0])
        self.center = np.array([c[0], c[1]])
        ax = matrix @ np.array([self.major_axis[0], self.major_axis[1], 0.0])
        self.major_axis = np.array([ax[0], ax[1]])
        # ratio, start_param, end_param giữ nguyên

    def bounds(self):
        x, y = self.center
        ax, ay = self.major_axis
        r = math.hypot(ax, ay)
        return (x-r, y-r, x+r, y+r)
