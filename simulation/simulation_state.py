from enum import Enum
class SimulationState(Enum):
    """Класс перечисления состояний, определяющих режим работы симуляции"""
    RUNNING = "Running"
    PAUSED = "Paused"
