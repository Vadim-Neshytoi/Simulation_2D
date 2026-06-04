import random

class WorldGenerator:
    """Класс, отвечающий за создание начального состояния мира и размещение объектов на карте"""

    def __init__(self, game_map, config):
        """:param self.game_map - объект карты, используемый генератором для размещения существ и объектов.
        :param self.config - содержит настройки генерации мира, включая типы сущностей и количество экземпляров каждого типа.
        :param self.all_cords - список всех координат карты, перемешанный случайным образом
        и используемый для размещения объектов без повторений.
        :param self.current_index - указатель на следующую свободную координату в списке all_cords."""
        self.game_map = game_map
        self.config = config
        self.all_cords = [(x, y) for y in range(game_map.height)
                          for x in range(game_map.width)]
        random.shuffle(self.all_cords)
        self.current_index = 0

    def generate_world(self):
        """Метод размещающий объекты и существ на случайных свободных клетках карты согласно настройкам конфигурации."""
        for obj_class, amount in self.config.items():
            for _ in range(amount):
                x, y = self.all_cords[self.current_index]
                obj = obj_class(x, y)
                self.game_map.set_entity(x, y, obj)
                self.current_index += 1

   





