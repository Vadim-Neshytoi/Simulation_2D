from actions.action import Action
from .world_generator import WorldGenerator


class WorldGenerationAction(Action):
    """Класс Action, выполняющий создание начального состояния мира с помощью WorldGenerator."""

    def execute(self, context):
        """Создаёт экземпляр WorldGenerator и запускает генерацию начального состояния мира согласно настройкам конфигурации."""
        game_map = context['map']
        config = context['config']
        generator = WorldGenerator(game_map, config)
        generator.generate_world()



