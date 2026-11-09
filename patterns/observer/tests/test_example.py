import unittest
from ..sensor import TemperatureSensor, Log


class ObserverTests(unittest.TestCase):
    def test_subscription_repeat_value_and_unsubscribe(self):
        sensor, log = TemperatureSensor(20), Log()
        sensor.subscribe(log)
        sensor.subscribe(log)
        self.assertEqual(log.values, [])
        for value in (21, 21, 22):
            sensor.set_value(value)
        self.assertEqual(log.values, [21, 22])
        sensor.unsubscribe(log)
        sensor.unsubscribe(log)
        sensor.set_value(23)
        self.assertEqual(log.values, [21, 22])

    def test_mutation_of_subscriptions_affects_next_delivery(self):
        sensor, later, added = TemperatureSensor(20), Log(), Log()
        class Editor:
            def update(self, value):
                sensor.unsubscribe(later)
                sensor.subscribe(added)
        sensor.subscribe(Editor())
        sensor.subscribe(later)
        sensor.set_value(21)
        self.assertEqual(later.values, [21])
        self.assertEqual(added.values, [])
        sensor.set_value(22)
        self.assertEqual(later.values, [21])
        self.assertEqual(added.values, [22])

    def test_error_stops_delivery_but_value_is_updated(self):
        sensor, log = TemperatureSensor(20), Log()
        class Broken:
            def update(self, value):
                raise RuntimeError("subscriber error")
        sensor.subscribe(Broken())
        sensor.subscribe(log)
        with self.assertRaises(RuntimeError):
            sensor.set_value(21)
        self.assertEqual(sensor.value, 21)
        self.assertEqual(log.values, [])
