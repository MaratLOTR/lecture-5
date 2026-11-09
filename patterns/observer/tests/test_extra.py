import unittest
from ..sensor import TemperatureSensor, Log
from ..observer_once import OneShotObserver


class OneShotTests(unittest.TestCase):
    def test_unsubscribe_does_not_skip_other_observers(self):
        sensor = TemperatureSensor(20)
        once, log = OneShotObserver(sensor), Log()
        sensor.subscribe(once)
        sensor.subscribe(log)
        sensor.set_value(21)
        sensor.set_value(22)
        self.assertEqual(once.values, [21])
        self.assertEqual(log.values, [21, 22])
