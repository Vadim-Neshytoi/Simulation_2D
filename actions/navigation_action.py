from actions.action import Action
from entities.intent import Intent
from entities.state import State
from pathfinding.bfs_pathfinder import BFSPathFinder


class NavigationAction(Action):
    """Класс отвечает за навигацию существ. Для существ, выбравших перемещение к цели,
     определяет следующую клетку маршрута и сохраняет её в destination"""

    def __init__(self):
        """:param self.path_finder Инициализирует объект BFSPathFinder, используемый для поиска маршрутов."""
        self.path_finder = BFSPathFinder()


    def execute(self, context):
        """Определяет следующую клетку маршрута для существ, выполняющих перемещение к выбранной цели."""
        game_map = context['map']
        creatures = game_map.get_all_creature()
        for creature in creatures:
            if creature.state == State.FLEE:
                continue
            if creature.intent != Intent.MOVE:
                continue
            if creature.target is None:
                creature.destination = None
                continue
            start_position = creature.get_coordinates()
            goal_cells = self.build_goal_cells(creature.target.get_coordinates(), game_map)
            next_step = self.path_finder.find_next_step(game_map, start_position, goal_cells)
            if next_step is not None:
                creature.destination = next_step
            else:
                creature.destination = None


    def build_goal_cells(self, coordinates, game_map):
        """Метод, Находит свободные соседние клетки вокруг цели и
         формирует множество конечных точек для алгоритма поиска пути."""
        goal_cells = set()
        neighbors = game_map.get_neighbors(*coordinates)
        for cord in neighbors:
            if not game_map.is_empty(*cord):
                continue
            goal_cells.add(cord)
        return goal_cells

















