import unittest
from ..scene import SceneSettings
from ..memento_limited_history import LimitedHistory


class LimitedHistoryTests(unittest.TestCase):
    def test_limit_discards_oldest_version(self):
        scene = SceneSettings(0)
        history = LimitedHistory(scene, limit=2)
        for value in (1, 2, 3):
            history.checkpoint()
            scene.brightness = value
        self.assertTrue(history.undo())
        self.assertEqual(scene.brightness, 2)
        self.assertTrue(history.undo())
        self.assertEqual(scene.brightness, 1)
        self.assertFalse(history.undo())
        self.assertTrue(history.redo())
        self.assertEqual(scene.brightness, 2)

    def test_invalid_limits(self):
        for limit in (0, -1, 1.5, True):
            with self.assertRaises(ValueError):
                LimitedHistory(SceneSettings(), limit)
