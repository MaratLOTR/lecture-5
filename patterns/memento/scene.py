"""Memento: независимый снимок настроек сцены. History — задание."""

from dataclasses import dataclass


@dataclass(frozen=True)
class SceneSnapshot:
    _brightness: int
    _target_temperature: float
    _devices: tuple[str, ...]


class SceneSettings:
    def __init__(self, brightness=50, target_temperature=22, devices=None):
        self.brightness = brightness
        self.target_temperature = target_temperature
        self.devices = list(devices) if devices is not None else []

    def save(self):
        return SceneSnapshot(self.brightness, self.target_temperature, tuple(self.devices))

    def restore(self, snapshot):
        if not isinstance(snapshot, SceneSnapshot):
            raise TypeError("Ожидается SceneSnapshot")
        self.brightness = snapshot._brightness
        self.target_temperature = snapshot._target_temperature
        self.devices = list(snapshot._devices)


class History:
    """Хранит только снимки, не читая их полей. Реализуйте методы по TASK.md."""

    def __init__(self, scene):
        self.scene = scene
        self._undo = []
        self._redo = []

    def checkpoint(self):
        # TODO: сохранить состояние ПЕРЕД изменением, очистить redo.
        raise NotImplementedError("Реализуйте checkpoint()")

    def undo(self):
        # TODO: вернуть bool и восстановить предыдущее состояние.
        raise NotImplementedError("Реализуйте undo()")

    def redo(self):
        # TODO: вернуть bool и восстановить отменённое состояние.
        raise NotImplementedError("Реализуйте redo()")
