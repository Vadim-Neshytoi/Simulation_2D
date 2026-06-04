import os


class Renderer:
    """Класс, отвечающий за визуализацию текущего состояния мира симуляции."""
    def __init__(self, game_map, default_value="🟫"):
        self.game_map = game_map
        self.default_value = default_value


    def render(self):
        """Выполняет перерисовку карты, отображая актуальное расположение всех сущностей."""
        os.system("cls")
        for y in range(self.game_map.height):
            row_string = []
            for x in range(self.game_map.width):
                obj = self.game_map.get_entity(x, y)
                renderer_char = self.default_value if obj is None else obj.char
                row_string.append(renderer_char.ljust(2))

            print("".join(row_string))






