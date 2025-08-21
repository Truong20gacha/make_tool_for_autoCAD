from dataclasses import dataclass
from typing import List
from .base import Entity

@dataclass
class DrawingObject:
    entities: List[Entity]

    def draw(self, msp):
        for ent in self.entities:
            ent.draw(msp)

    def transform(self, matrix):
        for ent in self.entities:
            ent.transform(matrix)

    def bounds(self):
        if not self.entities:
            return (0, 0, 0, 0)
        bboxes = [ent.bounds() for ent in self.entities]
        xmin = min(b[0] for b in bboxes)
        ymin = min(b[1] for b in bboxes)
        xmax = max(b[2] for b in bboxes)
        ymax = max(b[3] for b in bboxes)
        return (xmin, ymin, xmax, ymax)
