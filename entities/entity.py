class Entity:
    """Базовый класс всех объектов, существующих в мире симуляции."""

    def __init__(self, x, y, char):
        self._x = x
        self._y = y
        self.char = char

    def get_coordinates(self):
        return self._x, self._y

    def set_coordinates(self, x, y):
        self._x = x
        self._y = y

