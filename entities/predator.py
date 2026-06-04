from .creature import Creature
from .state import State
from .intent import Intent
from .performed_action_state import PerformedActionState


class Predator(Creature):
    """Класс хищника существа. Ищет травоядное для питания, гонится за травоядным и принимает решения
        о своих действиях в зависимости от окружающей обстановки."""

    def __init__(self, x, y, attack=10):
        super().__init__(x, y, char="🦁", max_HP = 20, max_energy = 20)
        self.HP = self.max_HP
        self.energy = self.max_energy
        self.attack = attack
        self.rest_threshold = self.max_energy * 0.1
        self.recovery_threshold = self.max_energy * 0.7
        self.move_cost = 1
        self.attack_cost = 1.5
        self.rest_recovery = 3
        self.kill_recovery = self.max_energy


    def make_move(self, game_map, visible_entities):
        """Определяет состояние, цель и намерение травоядного на текущий тик симуляции."""

        from .herbivore import Herbivore
        if self.state == State.RESTING:
            if self.energy >= self.recovery_threshold:
                self.state = State.SEARCH
                self.intent = None
            else:
                self.intent = None
                self.performed_action = PerformedActionState.REST
                return
        if self.energy <= self.rest_threshold:
            self.state = State.RESTING
            self.intent = None
            self.performed_action = PerformedActionState.REST
            return
        else:
            (nearest_herbivore_entity, nearest_herbivore_distance) = self.find_nearest_entity_data_by_type(Herbivore, visible_entities)
            current_target_valid = self.is_target_valid(game_map, visible_entities)
            current_target = self.target if current_target_valid else None
            if current_target is None:
                final_target = nearest_herbivore_entity
            elif nearest_herbivore_entity is None:
                final_target = current_target
            else:
                if nearest_herbivore_distance + 1 < self.manhattan_distance(self.get_coordinates(),current_target.get_coordinates()):
                    final_target = nearest_herbivore_entity
                else:
                    final_target = current_target
            if final_target is not None:
                final_distance = self.manhattan_distance(self.get_coordinates(), final_target.get_coordinates())
                self.state = State.CHASE
                if final_distance <= self.interaction_range:
                    self.intent = Intent.ATTACK
                    self.target = final_target
                else:
                    self.intent = Intent.MOVE
                    self.target = final_target
            else:
                self.state = State.SEARCH
                self.intent = Intent.MOVE
                self.target = None








