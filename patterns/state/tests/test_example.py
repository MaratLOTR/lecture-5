import unittest
from ..security import SecuritySystem, Disarmed, Armed, Alarm, Turnstile
from .. import security as m


class SecurityTests(unittest.TestCase):
    def test_all_supported_transitions_and_siren(self):
        table = {
            Disarmed: {"arm": getattr(m, "Arming", Armed), "motion": Disarmed, "disarm": Disarmed},
            Armed: {"arm": Armed, "motion": Alarm, "disarm": Disarmed},
            Alarm: {"arm": Alarm, "motion": Alarm, "disarm": Disarmed},
        }
        for initial, transitions in table.items():
            for event, expected in transitions.items():
                with self.subTest(initial=initial.__name__, event=event):
                    system = SecuritySystem()
                    system.transition_to(initial())
                    system.handle(event)
                    self.assertIsInstance(system.state, expected)
                    self.assertEqual(system.siren, expected is Alarm)

    def test_unknown_event_preserves_state(self):
        system = SecuritySystem()
        state = system.state
        with self.assertRaises(ValueError):
            system.handle("unknown")
        self.assertIs(system.state, state)
        self.assertFalse(system.siren)


class TurnstileTests(unittest.TestCase):
    def test_full_transition_table(self):
        for initial, event, result, final in (
            ("locked", "coin", "open", "unlocked"),
            ("locked", "passage", "blocked", "locked"),
            ("unlocked", "coin", "return_coin", "unlocked"),
            ("unlocked", "passage", "pass_and_close", "locked"),
        ):
            with self.subTest(initial=initial, event=event):
                turnstile = Turnstile()
                if initial == "unlocked":
                    turnstile.handle("coin")
                self.assertEqual(turnstile.handle(event), result)
                self.assertEqual(turnstile.state, final)

    def test_one_payment_cannot_buy_two_passages(self):
        turnstile = Turnstile()
        for event, result in (("coin", "open"), ("passage", "pass_and_close"), ("passage", "blocked")):
            self.assertEqual(turnstile.handle(event), result)
        with self.assertRaises(ValueError):
            turnstile.handle("unknown")
        self.assertEqual(turnstile.state, "locked")
