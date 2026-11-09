import unittest
from ..scene import SceneSettings, History


class HistoryTests(unittest.TestCase):
    def test_empty_history(self):
        history = History(SceneSettings())
        self.assertIs(history.undo(), False)
        self.assertIs(history.redo(), False)

    def test_undo_redo_and_new_branch(self):
        scene = SceneSettings(10, devices=["A"])
        history = History(scene)
        history.checkpoint()
        scene.brightness, scene.devices = 20, ["B"]
        history.checkpoint()
        scene.brightness, scene.devices = 30, ["C"]
        self.assertIs(history.undo(), True)
        self.assertEqual((scene.brightness, scene.devices), (20, ["B"]))
        self.assertTrue(history.undo())
        self.assertEqual(scene.brightness, 10)
        self.assertFalse(history.undo())
        self.assertTrue(history.redo())
        self.assertEqual(scene.brightness, 20)
        history.checkpoint()
        scene.brightness = 40
        self.assertFalse(history.redo())
        self.assertTrue(history.undo())
        self.assertEqual(scene.brightness, 20)
