if __package__:
    from . import scene as m
else:
    import scene as m


def demo():
    scene = m.SceneSettings(devices=["lamp"])
    snapshot = scene.save()
    scene.brightness = 10
    scene.devices.append("projector")
    print("После изменения:", scene.brightness, scene.devices)
    scene.restore(snapshot)
    print("После восстановления:", scene.brightness, scene.devices)


if __name__ == "__main__":
    demo()
