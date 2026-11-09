import unittest
from .. import heating


class FrostProtectionTests(unittest.TestCase):
    def test_threshold_and_independence_from_target(self):
        cls = getattr(heating, "FrostProtection", None)
        self.assertIsNotNone(cls, "ЗАДАНИЕ: добавьте FrostProtection, см. TASK.md")
        self.assertTrue(issubclass(cls, heating.HeatingStrategy))
        context = heating.Thermostat(heating.Eco())
        context.set_strategy(cls())
        for target in (-10, 22, 30):
            for current, expected in ((4, 25), (5, 0), (6, 0)):
                with self.subTest(current=current, target=target):
                    self.assertEqual(context.tick(current, target), expected)
