from enum import Enum


class Command(Enum):
    """Перечисление команд, используемых для управления выполнением симуляции."""

    RUN = "Run"
    PAUSE = "Pause"
    STEP = "Step"
    QUIT = "Quit"
