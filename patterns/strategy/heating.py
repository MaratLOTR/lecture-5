"""Strategy: смена алгоритма отопления у существующего термостата."""

from abc import ABC, abstractmethod

class HeatingStrategy(ABC):
    @abstractmethod
    def power(self, current, target):
        pass

class Eco(HeatingStrategy):
    def power(self, current, target):
        return 40 if current < target else 0

class Comfort(HeatingStrategy):
    def power(self, current, target):
        return min(100, max(
            0, (target - current) * 30
        ))

class Thermostat:
    def __init__(self, strategy: HeatingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def tick(self, current, target):
        return self.strategy.power(
            current, target
        )

# ЗАДАНИЕ: добавьте FrostProtection(HeatingStrategy), см. TASK.md.
