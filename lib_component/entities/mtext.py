from dataclasses import dataclass
import numpy as np
from typing import Dict, Any
from .base import Entity

@dataclass
class MText(Entity):
    text: str
    insert: np.ndarray  # [x, y]
    height: float
    attribs: Dict[str, Any]

    def draw(self, msp):
        msp.add_mtext(self.text, dxfattribs=self.attribs).set_location(tuple(self.insert))
