from entities.creature import Creature
import random


class Map:
    """Класс, представляющий игровую карту симуляции. Отвечает за хранение сущностей,
    их расположение и предоставление интерфейса для работы с клетками карты.
    Карта использует разреженное хранение данных: в словаре содержатся только занятые клетки,
     а отсутствие ключа означает пустую клетку."""
    def __init__(self, width, height):
        """:param self._cells - Словарь, хранящий все сущности карты. Ключом является кортеж координат (x, y),
         значением — объект, расположенный в данной клетке."""
        self.width = width
        self.height = height
        self._cells = {}


    def entity_is_exist(self, entity_object):
        x, y = entity_object.get_coordinates()
        if not self.is_in_bounds(x, y):
            return False
        else:
            entity = self.get_entity(x, y)
            return entity is entity_object

    def get_random_empty_cell(self):
        all_cords = [(x, y) for y in range(self.height)
                          for x in range(self.width)]
        random.shuffle(all_cords)
        for cord in all_cords:
            if self.is_empty(*cord):
                return cord
        return None

    def get_entities_in_radius(self, center, radius):
        x, y = center
        points_list = []
        x_min = max(0, x - radius)
        x_max = min(self.width - 1, x + radius)
        y_min = max(0, y - radius)
        y_max = min(self.height - 1, y + radius)
        for rx in range(x_min, x_max+1):
            for ry in range(y_min, y_max+1):
                if x == rx and y == ry:
                    continue
                obj = self.get_entity(rx, ry)
                if obj is not None:
                    points_list.append((obj, (rx, ry)))
        return points_list

    def get_neighbors(self, x, y):
        neighbors = []
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in direction:
            target_x = x + dx
            target_y = y + dy
            if not self.is_in_bounds(target_x, target_y):
                continue
            neighbors.append((target_x, target_y))
        return neighbors

    def get_all_creature(self):
        creature_list = []
        for obj in self._cells.values():
            if isinstance(obj, Creature):
                creature_list.append(obj)
        return creature_list

    def set_entity(self, x, y, value):
        """Устанавливает значение, если координаты в границах."""
        self._cells[(x,y)] = value

    def remove_object(self, x, y):
        self._cells.pop((x,y))

    def is_in_bounds(self, x, y):
        return not (x < 0 or x >= self.width) and not (y < 0 or y >= self.height)

    def get_entity(self, x, y):
        return self._cells.get((x, y))

    def is_empty(self, x, y):
        return self.get_entity(x, y) is None

    def move_entity(self, from_x, from_y, to_x, to_y):
        if not self.is_in_bounds(from_x, from_y):
            return False

        if not self.is_in_bounds(to_x, to_y):
            return False

        obj = self.get_entity(from_x, from_y)
        if obj is None:
            return False

        if not self.is_empty(to_x, to_y):
            return False

        self.remove_object(from_x, from_y)
        self.set_entity(to_x, to_y, obj)

        obj.set_coordinates(to_x, to_y)

        return True




