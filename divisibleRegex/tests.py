import unittest

from fsmToRegexHelpers import compute_regex_from_fsm


class TestCorrectness(unittest.TestCase):
    def test_correctness(self):
        alphabet = {'a', 'b', 'c'}
        initial_state = 'A'
        finals = {'C'}
        states = ['A', 'B', 'C']
        transitions = {
            'A': {
                'A': 'a',
                'B': 'b'
            },
            'B': {
                'A': 'c',
                'C': 'b'
            },
            'C': {
                'C': 'a',
                'A': 'b',
            }
        }
        inverted_transitions = {
            'A': {
                'A': 'a',
                'B': 'c',
                'C': 'b',
            },
            'B': {
                'A': 'b',
            },
            'C': {
                'C': 'a',
                'B': 'b',
            }
        }
        fsm = alphabet, states, initial_state, finals, transitions, inverted_transitions
        regex = compute_regex_from_fsm(fsm)
        self.assertEqual(regex, "^a*b(ca*b)*b((a|ba*b(ca*b)*b))*$")