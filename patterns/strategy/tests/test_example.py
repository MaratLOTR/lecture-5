import unittest
from ..heating import HeatingStrategy, Eco, Comfort, Thermostat


class StrategyTests(unittest.TestCase):
    def test_abstract_contract_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            HeatingStrategy()

    def test_runtime_replacement_preserves_context(self):
        context = Thermostat(Eco())
        self.assertEqual(context.tick(19, 22), 40)
        chosen = Comfort()
        context.set_strategy(chosen)
        self.assertIs(context.strategy, chosen)
        self.assertEqual(context.tick(19, 22), 90)

    def test_power_boundaries(self):
        for strategy in (Eco(), Comfort()):
            for current in (22, 23):
                self.assertEqual(strategy.power(current, 22), 0)
        self.assertEqual(Comfort().power(-10, 22), 100)
        self.assertEqual(Comfort().power(21, 22), 30)
