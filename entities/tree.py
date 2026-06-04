from .entity import Entity


class Tree(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, char="🌳")
