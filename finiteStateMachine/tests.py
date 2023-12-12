import unittest

from finiteStateMachine import FiniteStateMachine


class TestCorrectness(unittest.TestCase):
    def test_correctness(self):
        fsm = FiniteStateMachine({'a', 'b', 'c'})
        fsm.add_state('A')
        fsm.add_state('B')
        fsm.add_state('C')
        fsm.set_initial('A')
        fsm.set_final('C')
        fsm.add_transition('A', 'B', 'a')
        fsm.add_transition('B', 'B', 'b')
        fsm.add_transition('B', 'C', 'c')
        self.assertEqual(fsm.test('abbbbc'), True)
        self.assertEqual(fsm.test('babbbbc'), False)
        self.assertEqual(fsm.test('abbbbcc'), False)
        self.assertEqual(fsm.test('abbdbbc'), False)
