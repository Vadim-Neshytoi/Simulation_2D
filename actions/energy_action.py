from .action import Action
from entities.performed_action_state import PerformedActionState


class EnergyAction(Action):
    """Класс отвечает за изменение запаса энергии существ в соответствии с фактически выполненным действием.
    EnergyAction списывает энергию за перемещение и атаку, а также восстанавливает её во время отдыха,
    поедания травы и успешного убийства травоядного."""

    def execute(self, context):
        game_map = context['map']
        kills_this_tick = context['kills_this_tick']
        creatures = game_map.get_all_creature()
        creatures_copy = creatures.copy()
        for creature in creatures_copy:
            if creature.performed_action == PerformedActionState.MOVE:
                creature.energy -= creature.move_cost
            if creature.performed_action == PerformedActionState.ATTACK:
                creature.energy -= creature.attack_cost
                if creature.target.get_coordinates() in kills_this_tick:
                    creature.energy += creature.kill_recovery
            if creature.performed_action == PerformedActionState.EAT:
                creature.energy += creature.eat_recovery
            if creature.performed_action == PerformedActionState.REST:
                creature.energy += creature.rest_recovery
