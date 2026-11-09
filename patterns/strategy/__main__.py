if __package__:
    from . import heating as m
else:
    import heating as m


def demo():
    thermostat = m.Thermostat(m.Eco())
    print("Eco:", thermostat.tick(19, 22))
    thermostat.set_strategy(m.Comfort())
    print("Comfort:", thermostat.tick(19, 22))
    print("Выше цели:", thermostat.tick(23, 22))


if __name__ == "__main__":
    demo()
