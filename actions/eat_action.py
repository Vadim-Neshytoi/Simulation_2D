from .action import Action
from entities.herbivore import Herbivore
from entities.grass import Grass
from entities.intent import Intent
from entities.performed_action_state import PerformedActionState


class EatAction(Action):
    """Кдасс, ответственный за поедание травы травоядным"""

    def execute(self, context):
        game_map = context['map']
        creatures = game_map.get_all_creature()
        creatures_copy = creatures.copy()
        for creature in creatures_copy:
            if isinstance(creature, Herbivore) and creature.intent == Intent.EAT and creature.has_acted == False:
                target = creature.target
                if isinstance(target, Grass) and game_map.entity_is_exist(target):
                    creature_coordinates = creature.get_coordinates()
                    grass_coordinates = target.get_coordinates()
                    distance = creature.manhattan_distance(creature_coordinates, grass_coordinates)
                    if distance <= creature.interaction_range:
                        creature.performed_action = PerformedActionState.EAT
                        game_map.remove_object(*grass_coordinates)
                        context['grass_eaten_this_turn'] += 1
                        creature.HP = creature.max_HP
                        creature.energy = creature.max_energy
                    else:
                        creature.performed_action = None
                creature.has_acted = True





