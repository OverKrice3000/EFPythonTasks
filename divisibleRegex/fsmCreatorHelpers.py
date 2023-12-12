from typing import List, Tuple, Set

from typings import TransitionsT, FsmT
from utils import to_binary, find_greatest_pow_of_two


def compute_states_labels(squares_count: int) -> List[str]:
    states_count = pow(2, squares_count)
    states_labels = []
    for i in range(0, states_count):
        states_labels.append(to_binary(i, squares_count))
    return states_labels


def compute_finals_labels(squares_count: int) -> Set[str]:
    half_labels = compute_states_labels(int(squares_count / 2))
    finals_labels = set()
    for half in half_labels:
        finals_labels.add(half + '0' * int(squares_count / 2))
    return finals_labels


def compute_initial_label(squares_count: int) -> str:
    return '0' * squares_count


def compute_transition_between(state: str, digit: int, partition_list: List[bool]) -> str:
    computed_letter = digit
    state_label_len = len(state)
    state_label_half_len = int(state_label_len / 2)
    state_half_label = state[state_label_half_len: state_label_len]
    for i in range(0, state_label_half_len):
        if state_half_label[i] == '1' and partition_list[i]:
            computed_letter += 1
    computed_letter %= 2
    return state[1:] + str(computed_letter)


def compute_transitions(n: int, states: List[str]) -> Tuple[TransitionsT, TransitionsT]:
    n_binary_list = list(to_binary(n))
    n_binary_list.reverse()
    partition_list = []
    for i in n_binary_list:
        partition_list.append(True if i == '1' else False)
    transitions_map = dict()
    inverted_transitions_map = dict()
    for state in states:
        transitions_map[state] = dict()
        zero_transition = compute_transition_between(state, 0, partition_list)
        one_transition = compute_transition_between(state, 1, partition_list)
        transitions_map[state][zero_transition] = '0'
        transitions_map[state][one_transition] = '1'
        if inverted_transitions_map.get(zero_transition) is None:
            inverted_transitions_map[zero_transition] = dict()
        if inverted_transitions_map.get(one_transition) is None:
            inverted_transitions_map[one_transition] = dict()
        inverted_transitions_map[zero_transition][state] = '0'
        inverted_transitions_map[one_transition][state] = '1'

    return transitions_map, inverted_transitions_map


def compute_finite_state_machine_for(n: int) -> FsmT:
    greatest_pow_of_two = find_greatest_pow_of_two(n)
    squares_count = 2 * greatest_pow_of_two

    alphabet = {'0', '1'}
    states = compute_states_labels(squares_count)
    initial = compute_initial_label(squares_count)
    finals = compute_finals_labels(squares_count)
    (transitions, inverted_transitions) = compute_transitions(n, states)
    return alphabet, states, initial, finals, transitions, inverted_transitions
