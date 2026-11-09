import unittest
from .. import sensor as m


class HeatWarningTests(unittest.TestCase):
    def test_threshold_duplicates_and_unsubscribe(self):
        cls = getattr(m, "HeatWarning", None)
        self.assertIsNotNone(cls, "ЗАДАНИЕ: добавьте HeatWarning, см. TASK.md")
        sensor, warning = m.TemperatureSensor(20), cls()
        sensor.subscribe(warning)
        sensor.subscribe(warning)
        for value in (27, 28, 28, 29):
            sensor.set_value(value)
        self.assertEqual(warning.warnings, [28, 29])
        sensor.unsubscribe(warning)
        sensor.set_value(30)
        self.assertEqual(warning.warnings, [28, 29])
