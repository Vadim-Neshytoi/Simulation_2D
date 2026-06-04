from queue import Queue


class BFSPathFinder:
    """Класс, использующий алгоритм поиска в ширину (BFS) для определения следующего шага на пути к цели."""

    def find_next_step(self, game_map, start_position, goal_cells):
        """Выполняет поиск кратчайшего пути до одной из целевых клеток и возвращает следующий шаг на найденном маршруте.
        Алгоритм не строит полный маршрут для существа, а вычисляет только следующий шаг, необходимый для текущего тика симуляции.
        Также я не сделал find_next_step staticmethod, потому что хотел сохранить объектную архитектуру
        и возможность расширения навигационной системы. Instance-метод позволяет в будущем добавлять конфигурацию,
        состояние или альтернативные стратегии поиска пути без изменения интерфейса вызова.
        Что делает Pathfinder полноценным компонентом системы, а не просто утилитарной функцией."""
        if not goal_cells:
            return None
        if start_position in goal_cells:
            return None
        queue = Queue()
        queue.put(start_position)
        visited = {start_position}
        parent_map = {}
        while not queue.empty():
            current = queue.get()
            if current in goal_cells:
                next_step = current
                while parent_map[next_step] != start_position:
                    next_step = parent_map[next_step]
                return next_step
            else:
                neighbors = game_map.get_neighbors(*current)
                for neighbor in neighbors:
                    if neighbor in visited:
                        continue
                    if not game_map.is_empty(*neighbor):
                        continue
                    visited.add(neighbor)
                    parent_map[neighbor] = current
                    queue.put(neighbor)
        return None

