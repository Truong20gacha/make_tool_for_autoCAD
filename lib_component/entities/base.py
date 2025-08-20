from abc import ABC, abstractmethod

class Entity(ABC):
    @abstractmethod
    def draw(self, msp):
        pass

    @abstractmethod
    def transform(self, matrix):
        pass

    @abstractmethod
    def bounds(self):
        pass
