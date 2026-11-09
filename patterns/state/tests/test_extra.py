import unittest
from ..security import Armed
from ..state_entry_log import LoggedSecuritySystem


class EntryLogTests(unittest.TestCase):
    def test_history_and_siren_with_repeated_transitions(self):
        system = LoggedSecuritySystem()
        system.transition_to(Armed())
        system.transition_to(Armed())
        self.assertEqual(system.history, ["Disarmed", "Armed"])
        system.handle("motion")
        self.assertTrue(system.siren)
        system.handle("disarm")
        self.assertFalse(system.siren)
        self.assertEqual(system.history, ["Disarmed", "Armed", "Alarm", "Disarmed"])
