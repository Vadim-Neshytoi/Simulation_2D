from entities.rock import Rock
from entities.tree import Tree
from entities.grass import Grass
from entities.herbivore import Herbivore
from entities.predator import Predator
from .simulation_state import SimulationState
from controller.command import Command
from generation.world_generation_action import WorldGenerationAction
from actions.decision_action import DecisionAction
from actions.move_creatures_action import MoveCreaturesAction
from actions.attack_action import AttackAction
from actions.eat_action import EatAction
from actions.grass_respawn_action import GrassRespawnAction
from actions.herbivore_respawn_action import HerbivoreRespawnAction
from actions.navigation_action import NavigationAction
from actions.energy_action import EnergyAction


class Simulation:
    """Основной класс симуляции, управляющий состоянием мира, последовательностью действий и жизненным циклом симуляции."""

    def __init__(self, game_map):
        """:param self.config - конфигурация начальной генерации мира: определяет количество объектов и существ каждого типа.
        :param self.context - словарь общего контекста текущего тика симуляции, передаваемый между Action-классами.
        Содержит временные данные, такие как счётчики событий, состояние действий и глобальные параметры текущего тика.
        :param self.step_request - флаг запроса выполнения одного шага симуляции в пошаговом режиме.
        :param self.should_exit - Флаг завершения работы симуляции.
        :param self.init_actions - список действий, выполняемых один раз при запуске симуляции.
        :param self.turn_actions - список действий, выполняемых последовательно на каждом тике симуляции.
        Определяет полный цикл обновления мира от принятия решений до обновления энергии и респавна объектов."""
        self.game_map = game_map
        self.config = {Rock: 10,
                       Tree: 10,
                       Grass: 30,
                       Herbivore: 6,
                       Predator: 2}
        self.context = {"map": self.game_map,
                        "kills_this_tick": set(),
                        "grass_eaten_this_turn": 0,
                        "herbivore_deaths_this_turn": 0,
                        "config": self.config}
        self.state = SimulationState.PAUSED
        self.step_request = False
        self.should_exit = False
        self.init_actions = []
        self.turn_actions = [DecisionAction(),
                             AttackAction(),
                             EatAction(),
                             NavigationAction(),
                             MoveCreaturesAction(),
                             EnergyAction(),
                             GrassRespawnAction(),
                             HerbivoreRespawnAction(),
                             ]
        self.init_actions.append(WorldGenerationAction())

    def run_init_actions(self):
        """Метод выполняющий начальные действия симуляции, включая генерацию мира и первичную настройку состояния."""
        for action in self.init_actions:
            action.execute(self.context)

    def next_turn(self):
        """Метод выполняющий один тик симуляции, последовательно обрабатывая все действия из turn_actions."""
        self.context["grass_eaten_this_turn"] = 0
        self.context["herbivore_deaths_this_turn"] = 0
        creatures_list = self.game_map.get_all_creature()
        for creature in creatures_list:
            creature.has_acted = False
            creature.performed_action = None
        for action in self.turn_actions:
            action.execute(self.context)

    def process_command(self, cmd):
        """Метод обрабатывающий пользовательскую команду и изменяет состояние симуляции
        (запуск, пауза, пошаговый режим или завершение)."""
        if cmd == Command.RUN:
            if self.state == SimulationState.PAUSED:
                self.state = SimulationState.RUNNING
        elif cmd == Command.PAUSE:
            if self.state == SimulationState.RUNNING:
                self.state = SimulationState.PAUSED
        elif cmd == Command.STEP:
            if self.state == SimulationState.PAUSED:
                self.step_request = True
        elif cmd == Command.QUIT:
            self.should_exit = True






























