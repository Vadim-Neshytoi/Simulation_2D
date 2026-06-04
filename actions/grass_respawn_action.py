from .action import Action
from entities.grass import Grass


class GrassRespawnAction(Action):
    """Класс отвечает за восстановление популяции травы на карте.
     После каждого хода создаёт новую траву в случайных свободных клетках в количестве,
     равном числу съеденных за этот ход."""

    def execute(self, context):
        game_map = context['map']
        grass_eaten_this_turn = context['grass_eaten_this_turn']
        if grass_eaten_this_turn > 0:
            for i in range(grass_eaten_this_turn):
                empty_cell = game_map.get_random_empty_cell()
                if empty_cell is None:
                    continue
                new_grass = Grass(*empty_cell)
                game_map.set_entity(*empty_cell, new_grass)












