if __package__:
    from . import security as m
else:
    import security as m


def demo():
    security = m.SecuritySystem()
    for event in ("motion", "arm", "motion", "disarm"):
        security.handle(event)
        print(event, type(security.state).__name__, "сирена:", security.siren)
    turnstile = m.Turnstile()
    for event in ("passage", "coin", "coin", "passage", "passage"):
        print(event, turnstile.handle(event), turnstile.state)


if __name__ == "__main__":
    demo()
