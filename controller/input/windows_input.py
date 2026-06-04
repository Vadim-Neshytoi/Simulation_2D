import msvcrt
from controller.command import Command
from controller.input.input_provider import InputProvider


class WindowsInputProvider(InputProvider):
    """Реализация InputProvider для Windows.

    Использует модуль msvcrt для неблокирующего считывания нажатий клавиш.
    Преобразует клавиши (r, p, s, q) в соответствующие команды симуляции.

    Поддерживает режим реального времени без необходимости нажатия Enter."""
    def get_command(self):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'r':
                return Command.RUN
            elif key == b'p':
                return Command.PAUSE
            elif key == b's':
                return Command.STEP
            elif key == b'q':
                return Command.QUIT
        return None
