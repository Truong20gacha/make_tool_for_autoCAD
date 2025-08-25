from dataclasses import dataclass
import numpy as np
from typing import Dict, Any
from .base import Entity

@dataclass
class BlockRef(Entity):
    block_name: str
    insert: np.ndarray  # [x, y]
    scale: float
    rotation: float
    attribs: Dict[str, Any]

    def draw(self, msp):
        msp.add_blockref(self.block_name, tuple(self.insert),
                         dxfattribs=self.attribs)
        # Nếu muốn scale/rotation nâng cao, phải apply transform ngoài
