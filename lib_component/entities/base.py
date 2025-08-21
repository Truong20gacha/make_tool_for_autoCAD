class Entity:
    def draw(self, msp):
        raise NotImplementedError

    def transform(self, matrix):
        raise NotImplementedError

    def bounds(self):
        raise NotImplementedError
