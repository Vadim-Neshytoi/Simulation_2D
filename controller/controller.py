from simulation.simulation_state import SimulationState
from .command_queue import CommandQueue
import time


class Controller:
    """Класс, обрабатывающий пользовательский ввод и передающий команды управления в симуляцию через очередь команд.
    Класс не содержит логики симуляции и служит только для управления её выполнением и пользовательским вводом."""

    def __init__(self, simulation, renderer, input_provider):
        """:param self.command_queue - Очередь команд управления симуляцией, поступающих от пользователя
        :param self.simulation - Объект симуляции, содержащий состояние мира и логику его обновления.
        :param self.renderer - Объект, отвечающий за визуализацию текущего состояния симуляции.
        :param self.is_running - Флаг, определяющий, выполняется ли основной цикл приложения."""
        self.command_queue = CommandQueue()
        self.input_provider = input_provider
        self.simulation = simulation
        self.renderer = renderer
        self.is_running = True

    def show_start_menu(self):
        """Метод выводит меню доступных команд управления симуляцией"""
        print("Меню команд: \n[R] - Запустить симуляцию \n[S] - Пошаговый режим \n[P] - Пауза \n[Q] - Выйти")


    def process_input(self):
        """Получает команду от InputProvider и добавляет её в очередь команд.

        Отделяет логику симуляции от способа ввода,
        обеспечивая кроссплатформенность системы."""
        cmd = self.input_provider.get_command()
        if cmd:
            self.command_queue.enqueue(cmd)


    def update(self):
        """Обрабатывает команды управления, обновляет состояние симуляции и при необходимости выполняет один шаг симуляции.
        :param world_updated - Флаг, сигнализирующий о том, изменилось ли состояние симуляции в текущем обновлении
         и требуется ли перерисовка мира."""
        world_updated = False
        cmd = self.command_queue.dequeue()
        if cmd:
            self.simulation.process_command(cmd)
        if self.simulation.should_exit:
            self.is_running = False
        if self.simulation.state == SimulationState.RUNNING:
            self.simulation.next_turn()
            world_updated = True
        if self.simulation.step_request :
            if self.simulation.state == SimulationState.PAUSED:
                self.simulation.next_turn()
                world_updated = True
                self.simulation.step_request = False
        return world_updated

    def run(self):
        """Запускает основной цикл работы приложения: инициализацию, обработку ввода,
         обновление симуляции и отрисовку состояния мира."""
        self.simulation.run_init_actions()
        self.renderer.render()
        self.show_start_menu()
        while self.is_running:
            self.process_input()
            update = self.update()
            if update:
                self.renderer.render()
                self.show_start_menu()
            time.sleep(0.5)





