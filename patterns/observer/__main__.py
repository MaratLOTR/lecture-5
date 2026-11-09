if __package__:
    from . import sensor as m
else:
    import sensor as m


def demo():
    sensor = m.TemperatureSensor(20)
    display, log = m.Display(), m.Log()
    sensor.subscribe(display)
    sensor.subscribe(log)
    sensor.set_value(21)
    sensor.set_value(21)
    sensor.unsubscribe(display)
    sensor.set_value(22)
    print("Журнал:", log.values)


if __name__ == "__main__":
    demo()
