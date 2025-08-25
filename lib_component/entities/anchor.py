from dataclasses import dataclass
import numpy as np
from typing import Dict, Any
from .base import Entity

@dataclass
class Anchor(Entity):
    tag: str
    insert: np.ndarray  # [x, y]
    attribs: Dict[str, Any]

    def draw(self, msp):
        # Vẽ 1 hình tròn nhỏ ở vị trí anchor để debug
        msp.add_circle(tuple(self.insert), 20, dxfattribs={"color": 1, "layer": "ANCHOR"})
