from collections import deque


class CommandQueue:
    """Очередь команд управления симуляцией."""

    def __init__(self):
        """:param queue: Очередь (deque), хранящая команды управления симуляцией в порядке их поступления."""
        self.queue = deque([])


    def enqueue(self, command):
        """Метод добавляет команду в конец очереди."""
        self.queue.append(command)

    def dequeue(self):
        """Метод извлекает и возвращает первую команду из очереди. Если очередь пуста, возвращает None."""
        if self.is_empty_queue():
            return None
        return self.queue.popleft()

    def is_empty_queue(self):
        """Метод возвращает True, если очередь команд пуста, иначе False."""
        return not bool(self.queue)
