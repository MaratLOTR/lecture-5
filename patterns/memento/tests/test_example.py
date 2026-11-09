import unittest
from dataclasses import FrozenInstanceError
from ..scene import SceneSettings


class SnapshotTests(unittest.TestCase):
    def test_snapshot_is_independent_and_restores_all_fields(self):
        devices = ["lamp"]
        scene = SceneSettings(50, 22, devices)
        devices.append("external")
        self.assertEqual(scene.devices, ["lamp"])
        snapshot = scene.save()
        scene.brightness, scene.target_temperature = 10, 18
        scene.devices.append("projector")
        scene.restore(snapshot)
        self.assertEqual((scene.brightness, scene.target_temperature, scene.devices), (50, 22, ["lamp"]))
        scene.devices.clear()
        scene.restore(snapshot)
        self.assertEqual(scene.devices, ["lamp"])

    def test_snapshot_is_frozen(self):
        snapshot = SceneSettings().save()
        with self.assertRaises(FrozenInstanceError):
            snapshot._brightness = 10

    def test_invalid_snapshot_does_not_partially_restore(self):
        scene = SceneSettings()
        before = scene.save()
        with self.assertRaises(TypeError):
            scene.restore(object())
        self.assertEqual(scene.save(), before)
