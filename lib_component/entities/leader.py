from dataclasses import dataclass
import numpy as np
from typing import Dict, Any
from .base import Entity

@dataclass
class Leader(Entity):
    vertices: np.ndarray  # [[x1, y1], [x2, y2], ...]
    attribs: Dict[str, Any]

    def draw(self, msp):
        msp.add_lwpolyline([tuple(pt) for pt in self.vertices], dxfattribs=self.attribs)
