"""Дополнительно: запись смены состояний без дублирования логики сирены.

LoggedSecuritySystem наследует SecuritySystem. history начинается со строки
Disarmed. Переопределите transition_to(): вызовите родительский метод и добавьте
имя нового состояния, только если его тип отличается от предыдущего.
"""
from .security import SecuritySystem


class LoggedSecuritySystem(SecuritySystem):
    def __init__(self):
        super().__init__()
        self.history = [type(self.state).__name__]

    def transition_to(self, state):
        # TODO: делегировать родителю и записать реальную смену состояния.
        raise NotImplementedError("Реализуйте журнал переходов")
