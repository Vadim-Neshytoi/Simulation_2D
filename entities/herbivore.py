from .creature import Creature
from .grass import Grass
from .state import State
from .intent import Intent
from .performed_action_state import PerformedActionState


class Herbivore(Creature):
    """Класс травоядного существа. Ищет траву для питания, избегает хищников и принимает решения
    о своих действиях в зависимости от окружающей обстановки."""

    def __init__(self, x, y):
        super().__init__(x, y, char="🦓", max_HP = 20, max_energy = 20)
        self.HP = self.max_HP
        self.energy = self.max_energy
        self.rest_threshold = self.max_energy * 0.1
        self.recovery_threshold = self.max_energy * 0.5
        self.move_cost = 2
        self.rest_recovery = 2
        self.eat_recovery = self.max_energy



    def make_move(self, game_map, visible_entities):
        """Определяет состояние, цель и намерение травоядного на текущий тик симуляции."""

        from .predator import Predator
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
            predator_entity = self.find_nearest_entity_data_by_type(Predator, visible_entities)[0]
            (nearest_grass_entity, nearest_grass_distance) = self.find_nearest_entity_data_by_type(Grass, visible_entities)
            current_target_valid = self.is_target_valid(game_map, visible_entities)
            current_food_target = self.target if current_target_valid else None
            if predator_entity is not None:
                self.state = State.FLEE
                self.intent = Intent.MOVE
                self.destination = self.find_escape_position(game_map, predator_entity)
                self.target = predator_entity
                return
            elif nearest_grass_entity is None:
                final_target = current_food_target
            elif current_food_target is None:
                final_target = nearest_grass_entity
            else:
                if nearest_grass_distance + 1 < self.manhattan_distance(self.get_coordinates(), current_food_target.get_coordinates()):
                    final_target = nearest_grass_entity
                else:
                    final_target = current_food_target
            if final_target is not None:
                final_distance = self.manhattan_distance(self.get_coordinates(), final_target.get_coordinates())
                self.state = State.SEARCH
                if final_distance <= self.interaction_range:
                    self.intent = Intent.EAT
                    self.target = final_target
                else:
                    self.intent = Intent.MOVE
                    self.target = final_target
            else:
                self.state = State.SEARCH
                self.intent = Intent.MOVE
                self.target = None

    def find_escape_position(self, game_map, predator_entity):
        """Выбирает наиболее безопасную соседнюю клетку для бегства от хищника."""

        x, y = self.get_coordinates()
        predator_coordinates = predator_entity.get_coordinates()
        neighbors = game_map.get_neighbors(x, y)
        fallback = self.previous_position
        valid_moves = []
        for neighbor in neighbors:
            if game_map.is_empty(*neighbor):
                valid_moves.append(neighbor)
        if not valid_moves:
            return x, y
        if fallback in valid_moves:
            valid_moves.remove(fallback)
        if valid_moves:
            best_moves = max(valid_moves, key=lambda p: self.manhattan_distance(predator_coordinates, p))
            return best_moves
        else:
            return fallback


