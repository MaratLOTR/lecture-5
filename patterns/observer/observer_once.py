"""Дополнительно: OneShotObserver получает одно событие и отписывается.

update(value) добавляет значение в values и вызывает sensor.unsubscribe(self).
Остальные подписчики должны получить это же событие.
"""

class OneShotObserver:
    def __init__(self, sensor):
        self.sensor = sensor
        self.values = []

    def update(self, value):
        # TODO: сохранить значение и отписаться.
        raise NotImplementedError("Реализуйте одноразовую подписку")
