from dataclasses import dataclass
import numpy as np
from .base import Entity

@dataclass
class Text(Entity):
    text: str
    insert: np.ndarray
    height: float
    attribs: dict

    def draw(self, msp):
        msp.add_text(self.text, dxfattribs={
            "insert": (self.insert[0], self.insert[1]),
            "height": self.height,
            **self.attribs
        })

    def transform(self, matrix):
        p = matrix @ [self.insert[0], self.insert[1], 1.0]
        self.insert = [p[0], p[1]]
        sx = np.linalg.norm(matrix @ [1, 0, 0] - matrix @ [0, 0, 0])
        self.height *= sx

    def bounds(self):
        w = 0.6 * self.height * len(self.text)
        h = self.height
        x, y = self.insert
        return (x, y, x + w, y + h)
