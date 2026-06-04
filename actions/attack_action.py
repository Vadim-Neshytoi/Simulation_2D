from entities import herbivore
from .action import Action
from entities.predator import Predator
from entities.herbivore import Herbivore
from entities.intent import Intent
from entities.performed_action_state import PerformedActionState


class AttackAction(Action):
    """Кдасс, ответственный за выполнение атаки хищником травоядного
        :param kills_this_tick множество, хранящее координаты травоядных, убитых за один тик"""

    def execute(self, context):
        game_map = context['map']
        kills_this_tick = context['kills_this_tick']
        creatures = game_map.get_all_creature()
        creatures_copy = creatures.copy()
        for creature in creatures_copy:
            if isinstance(creature, Predator) and creature.intent == Intent.ATTACK and creature.has_acted == False:
                if creature.energy < creature.attack_cost:
                    creature.performed_action = None
                    creature.has_acted = True
                    continue
                else:
                    target = creature.target
                    if isinstance(target, Herbivore) and game_map.entity_is_exist(target):
                        creature_coordinates = creature.get_coordinates()
                        herbivore_coordinates = target.get_coordinates()
                        distance = creature.manhattan_distance(creature_coordinates, herbivore_coordinates)
                        if distance <= creature.interaction_range:
                            creature.performed_action = PerformedActionState.ATTACK
                            target.HP -=creature.attack
                            if target.HP <= 0:
                                kills_this_tick.add(herbivore_coordinates)
                                game_map.remove_object(*herbivore_coordinates)
                                context["herbivore_deaths_this_turn"] += 1
                                creature.HP = creature.max_HP
                        else:
                            creature.performed_action = None
                    creature.has_acted = True

















