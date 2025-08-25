from dataclasses import dataclass
import numpy as np
from typing import Dict, Any
from .base import Entity

@dataclass
class Point(Entity):
    location: np.ndarray  # [x, y]
    attribs: Dict[str, Any]

    def draw(self, msp):
        msp.add_point(tuple(self.location), dxfattribs=self.attribs)
