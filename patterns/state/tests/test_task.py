import unittest
from .. import security as m


class ArmingTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(getattr(m, "Arming", None), "ЗАДАНИЕ: добавьте Arming и timeout, см. TASK.md")

    def test_waiting_then_alarm(self):
        system = m.SecuritySystem()
        system.handle("arm")
        for event in ("arm", "motion"):
            system.handle(event)
            self.assertIsInstance(system.state, m.Arming)
            self.assertFalse(system.siren)
        system.handle("timeout")
        self.assertIsInstance(system.state, m.Armed)
        system.handle("motion")
        self.assertIsInstance(system.state, m.Alarm)
        self.assertTrue(system.siren)

    def test_cancellation_and_timeout_elsewhere(self):
        system = m.SecuritySystem()
        system.handle("arm")
        system.handle("disarm")
        self.assertIsInstance(system.state, m.Disarmed)
        for state in (m.Disarmed(), m.Armed(), m.Alarm()):
            system.transition_to(state)
            system.handle("timeout")
            self.assertIs(system.state, state)
            self.assertEqual(system.siren, isinstance(state, m.Alarm))
