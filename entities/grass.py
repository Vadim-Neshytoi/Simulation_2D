from .entity import Entity


class Grass(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, char="🌾")
