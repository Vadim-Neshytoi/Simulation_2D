from enum import Enum


class Intent(Enum):
    """Класс перечисления намерений существа на текущий тик симуляции"""

    ATTACK = "Attack"
    EAT = "Eat"
    MOVE = "Move"