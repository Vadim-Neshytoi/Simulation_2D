from .entity import Entity
from .state import State
from abc import ABC, abstractmethod


class Creature(Entity, ABC):
    """Абстрактный базовый класс всех существ симуляции.
    Содержит общие характеристики, состояние и логику, используемую хищниками и травоядными."""

    def __init__(self, x, y, char, max_HP, max_energy):
        """:param self.rest_threshold - пороговое значение, при котором существо начинает отдыхать
        :param self.recovery_threshold -значение энергии, при достижении которого существо завершает отдых
         и возвращается к обычному поведению.
        :param self.radius - радиус обзора существа, определяющий область поиска видимых объектов.
        :param self.interaction_range - максимальная дистанция, на которой существо может взаимодействовать с целью.
        :param self.has_acted - флаг, показывающий, выполнило ли существо своё действие в текущем тике.
        :param self.destination - Промежуточная клетка назначения, в которую существо должно переместиться в текущем тике.
         Может отличаться от конечной цели."""
        super().__init__(x, y, char)
        self.max_HP = max_HP
        self.max_energy = max_energy
        self.rest_threshold = None
        self.recovery_threshold = None
        self.radius = 2
        self.interaction_range = 1
        self.state = State.SEARCH
        self.has_acted = False
        self.target = None
        self.intent = None
        self.destination = None
        self.performed_action = None
        self.previous_position = None


    def prepare_turn(self, game_map):
        """Метод подготавливающий существо к новому тику симуляции,
        сбрасывает временные данные и запускает процесс принятия решения."""
        self.intent = None
        self.destination = None
        center = self.get_coordinates()
        visible_entities = game_map.get_entities_in_radius(center, self.radius)
        self.make_move(game_map, visible_entities)

    @abstractmethod
    def make_move(self, game_map, visible_entities):
        """Абстрактный метод принятия решения существом.
        Определяет состояние, цель и намерение существа на текущий тик симуляции."""
        pass


    def is_target_valid(self, game_map, visible_entities):
        """Метод проверяющий, существует ли текущая цель и находится ли она в зоне видимости существа."""
        if self.target is None:
            return False
        if not game_map.entity_is_exist(self.target):
            return False
        for entity, cord in visible_entities:
            if entity is self.target:
                return True
        return False


    def find_nearest_entity_data_by_type(self, target_type, visible_entities):
        """Ищет ближайшую сущность указанного типа среди видимых объектов и возвращает её вместе с расстоянием до неё."""
        best_target = None
        best_distance = float('inf')
        creature_cords = self.get_coordinates()
        for obj, cord in visible_entities:
            if isinstance(obj, target_type):
                distance = self.manhattan_distance(creature_cords, cord)
                if distance < best_distance:
                    best_distance = distance
                    best_target = obj
        if best_distance == float('inf'):
            return None, None
        return best_target, best_distance


    @staticmethod
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])






























