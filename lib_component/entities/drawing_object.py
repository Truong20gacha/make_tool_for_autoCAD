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
        return (min(b[0] for b in bboxes),
                min(b[1] for b in bboxes),
                max(b[2] for b in bboxes),
                max(b[3] for b in bboxes))
