"""Дополнительно: история хранит не больше limit предыдущих состояний.

Переопределите checkpoint(): вызовите родителя и удалите старейшие элементы
_undo сверх limit. limit — положительное целое, иначе ValueError.
Сначала выполните основное задание History.
"""
from .scene import History


class LimitedHistory(History):
    def __init__(self, scene, limit=3):
        if not isinstance(limit, int) or isinstance(limit, bool) or limit <= 0:
            raise ValueError("limit должен быть положительным целым")
        super().__init__(scene)
        self.limit = limit

    def checkpoint(self):
        # TODO: сохранить снимок и ограничить глубину истории.
        raise NotImplementedError("Реализуйте ограничение истории")
