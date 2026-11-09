"""Observer: синхронная подписка на изменения температуры."""

class TemperatureSensor:
    def __init__(self, value):
        self.value = value
        self._observers = []

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    # Продолжение TemperatureSensor
    def set_value(self, value):
        if value == self.value:
            return
        self.value = value
        for observer in tuple(self._observers):
            observer.update(value)

class Display:
    def update(self, value):
        print(f"Temperature: {value}")

class Log:
    def __init__(self):
        self.values = []

    def update(self, value):
        self.values.append(value)

# ЗАДАНИЕ: добавьте HeatWarning, см. TASK.md.
