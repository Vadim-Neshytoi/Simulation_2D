import os
import sys


class Renderer:
    """Класс, отвечающий за визуализацию текущего состояния мира симуляции."""
    def __init__(self, game_map, default_value="🟫"):
        self.game_map = game_map
        self.default_value = default_value

    def clear_screen(self):
        """Метод очищающий экран терминала в зависимости от того, на какой операционной системе запущена симуляция"""
        if sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")

    def render(self):
        """Выполняет перерисовку карты, отображая актуальное расположение всех сущностей."""
        self.clear_screen()
        for y in range(self.game_map.height):
            row_string = []
            for x in range(self.game_map.width):
                obj = self.game_map.get_entity(x, y)
                renderer_char = self.default_value if obj is None else obj.char
                row_string.append(renderer_char.ljust(2))

            print("".join(row_string))






