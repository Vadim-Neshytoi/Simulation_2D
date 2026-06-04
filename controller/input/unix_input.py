from controller.input.input_provider import InputProvider
from controller.command import Command


class UnixInputProvider(InputProvider):
    """ Реализация InputProvider для Unix-подобных систем (Linux/macOS).

    Использует стандартный ввод (input) для получения команд от пользователя.
    Требует подтверждения ввода клавишей Enter.

    Простой кроссплатформенный вариант ввода для запуска симуляции
    без зависимости от Windows-специфичных библиотек."""
    def get_command(self):
        cmd = input("Command (r/p/s/q): ").strip().lower()
        if cmd == 'r':
            return Command.RUN
        elif cmd == 'p':
            return Command.PAUSE
        elif cmd == 's':
            return Command.STEP
        elif cmd == 'q':
            return Command.QUIT

        return None
