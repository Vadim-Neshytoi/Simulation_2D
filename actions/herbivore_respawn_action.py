from .action import Action
from entities.herbivore import Herbivore


class HerbivoreRespawnAction(Action):
    """Класс отвечает за восстановление популяции травоядных на карте.
     После каждого хода создаёт новых травоядных в случайных свободных клетках в количестве,
     равном числу убитых за этот ход."""

    def execute(self, context):
        game_map = context['map']
        herbivore_deaths_this_turn = context['herbivore_deaths_this_turn']
        if herbivore_deaths_this_turn > 0:
            for i in range(herbivore_deaths_this_turn):
                empty_cell = game_map.get_random_empty_cell()
                if empty_cell is None:
                    continue
                new_herbivore = Herbivore(*empty_cell)
                game_map.set_entity(*empty_cell, new_herbivore)





