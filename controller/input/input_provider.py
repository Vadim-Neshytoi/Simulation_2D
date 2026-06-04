import msvcrt
from abc import ABC, abstractmethod


class InputProvider(ABC):
    """Абстрактный интерфейс источника пользовательских команд.

    Определяет единый контракт для всех реализаций ввода,
    независимо от платформы (Windows, Linux, macOS).

    Используется Controller для получения команд управления симуляцией
    без привязки к конкретной операционной системе"""
    @abstractmethod
    def get_command(self):
        pass