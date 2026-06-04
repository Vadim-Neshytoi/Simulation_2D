from .action import Action
from entities.intent import Intent
from entities.performed_action_state import PerformedActionState
import random


class MoveCreaturesAction(Action):

    """Класс отвечает за выполнение перемещения существ по карте.
     Обрабатывает всех существ с намерением MOVE и перемещает их в выбранную клетку при соблюдении условий движения."""

    def execute(self, context):
        game_map = context["map"]
        creatures = game_map.get_all_creature()
        creatures_copy = creatures.copy()
        for creature in creatures_copy:
            if creature.intent != Intent.MOVE:
                continue
            if creature.has_acted:
                continue

            if creature.energy < creature.move_cost:
                creature.performed_action = None
                creature.has_acted = True
                continue
            else:
                start_position = creature.get_coordinates()
                if creature.destination is not None:
                    move_success = game_map.move_entity(*start_position, *creature.destination)
                    creature.has_acted = True
                    if move_success:
                        creature.performed_action = PerformedActionState.MOVE
                        creature.previous_position = start_position
                    else:
                        creature.performed_action = None
                    continue
                else:
                    random_step = self.random_move(game_map, creature)
                    move_success = game_map.move_entity(*start_position, *random_step)
                    creature.has_acted = True
                    if move_success:
                        creature.performed_action = PerformedActionState.MOVE
                    else:
                        creature.performed_action = None
                    continue


    def random_move(self, game_map, creature):
        """Метод находит свободные соседние клетки и случайным образом выбирает одну из них для перемещения.
             Если доступных клеток нет, возвращает текущую позицию существа"""
        x, y = creature.get_coordinates()
        neighbors = game_map.get_neighbors(x, y)
        empty_neighbors = []
        for neighbor in neighbors:
            if not game_map.is_empty(*neighbor):
                continue
            else:
                empty_neighbors.append(neighbor)
        if empty_neighbors:
            random.shuffle(empty_neighbors)
            return empty_neighbors[0]
        else:
            return x, y