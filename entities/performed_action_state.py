from enum import Enum


class PerformedActionState(Enum):
    """Класс перечисления действий, фактически выполненных существом в текущем ходе симуляции.
     Используется системой энергии для расчёта расхода и восстановления энергии."""

    MOVE = "Move"
    ATTACK = "Attack"
    EAT = "Eat"
    REST = "Rest"