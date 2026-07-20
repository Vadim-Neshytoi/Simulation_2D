from __future__ import annotations
from typing import TYPE_CHECKING, Generator

if TYPE_CHECKING:
    from entities.entity import Entity


from entities.creature import Creature
import random


class Map:
    """Класс, представляющий игровую карту симуляции. Отвечает за хранение сущностей,
    их расположение и предоставление интерфейса для работы с клетками карты.
    Карта использует разреженное хранение данных: в словаре содержатся только занятые клетки,
     а отсутствие ключа означает пустую клетку."""
    def __init__(self, width: int, height: int) -> None:
        """:param self._cells - Словарь, хранящий все сущности карты. Ключом является кортеж координат (x, y),
         значением — объект, расположенный в данной клетке."""
        self.width = width
        self.height = height
        self._cells: dict[tuple[int, int], Entity] = {}


    def entity_is_exist(self, entity_object: Entity) -> bool:
        x, y = entity_object.get_coordinates()
        if not self.is_in_bounds(x, y):
            return False
        else:
            entity = self.get_entity(x, y)
            return entity is entity_object

    def iter_empty_cells(self) -> Generator[tuple[int, int]]:
        for y in range(self.height):
            for x in range(self.width):
                if self.is_empty(x, y):
                    yield x, y

    def get_random_empty_cell(self) -> tuple[int, int] | None:
        empty_cells = list(self.iter_empty_cells())
        if not empty_cells:
            return None
        return random.choice(empty_cells)

    def get_entities_in_radius(self, center: tuple[int, int], radius: int) -> list[tuple[Entity, tuple[int, int]]]:
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

    def get_neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        neighbors = []
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in direction:
            target_x = x + dx
            target_y = y + dy
            if not self.is_in_bounds(target_x, target_y):
                continue
            neighbors.append((target_x, target_y))
        return neighbors

    def get_all_creatures(self) -> list[Creature]:
        creature_list = []
        for obj in self._cells.values():
            if isinstance(obj, Creature):
                creature_list.append(obj)
        return creature_list

    def set_entity(self, x: int, y: int, value: Entity) -> bool:
        """Устанавливает значение, если координаты в границах."""
        if self.can_place_entity(x, y):
            self._cells[(x,y)] = value
            value.set_coordinates(x, y)
            return True
        return False

    def remove_object(self, x: int, y: int) -> bool:
        if  self.is_in_bounds(x, y) and not self.is_empty(x, y):
            self._cells.pop((x,y))
            return True
        return False

    def can_place_entity(self, x: int, y: int) -> bool:
        if self.is_in_bounds(x, y) and self.is_empty(x, y):
            return True
        return False

    def is_in_bounds(self, x: int, y: int) -> bool:
        return not (x < 0 or x >= self.width) and not (y < 0 or y >= self.height)

    def get_entity(self, x: int, y: int) -> Entity | None:
        return self._cells.get((x, y))

    def is_empty(self, x: int, y: int) -> bool:
        return self.get_entity(x, y) is None

    def move_entity(self, from_x: int, from_y: int, to_x: int, to_y: int) -> bool:
        obj = self.get_entity(from_x, from_y)
        if obj is None:
            return False
        if self.can_place_entity(to_x, to_y):
            self.remove_object(from_x, from_y)
            self.set_entity(to_x, to_y, obj)
            return True
        else:
            return False




