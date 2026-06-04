from .action import Action


class DecisionAction(Action):
    """Кдасс инициирует подготовку существа к ходу. Каждое существо самостоятельно определяет свое состояние,
    цель и намерение на текущий тик"""

    def execute(self, context):
        game_map = context["map"]
        creatures = game_map.get_all_creature()
        for creature in creatures:
            creature.prepare_turn(game_map)
























