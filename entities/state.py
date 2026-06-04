from enum import Enum


class State(Enum):
    """Класс перечисления внутренних состояний существа, определяющих его текущее поведение."""

    SEARCH = "Search"
    CHASE = "Chase"
    FLEE = "Flee"
    RESTING = "Resting"