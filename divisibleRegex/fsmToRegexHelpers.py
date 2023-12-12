from typing import Tuple, List, Optional

from typings import FsmT, TransitionsT


def add_single_initial_state(fsm: FsmT) -> FsmT:
    new_initial = 'INITIAL'
    (alphabet, states, initial_state, finals, transitions, inverted_transitions) = fsm
    states.append(new_initial)
    transitions[new_initial] = dict()
    inverted_transitions[new_initial] = dict()
    transitions[new_initial][initial_state] = '^'
    inverted_transitions[initial_state][new_initial] = '^'
    return alphabet, states, new_initial, finals, transitions, inverted_transitions


def add_single_final_state(fsm: FsmT) -> FsmT:
    new_final = 'FINAL'
    (alphabet, states, initial_state, finals, transitions, inverted_transitions) = fsm
    states.append(new_final)
    transitions[new_final] = dict()
    inverted_transitions[new_final] = dict()
    for final in finals:
        transitions[final][new_final] = '$'
        inverted_transitions[new_final][final] = '$'
    return alphabet, states, initial_state, {new_final}, transitions, inverted_transitions


def create_reduced_transition(prev_cur_state_transition_label: str, cur_next_state_transition_label: str,
                              prev_next_state_transition_label: Optional[str],
                              circular_transition_label: Optional[str], named_groups: bool = False) -> str:
    open_par = "(" if named_groups else "(?:"
    left_label = ''
    right_label = ''
    transition_label = ''
    if prev_next_state_transition_label is not None and prev_next_state_transition_label != '':
        left_label += prev_next_state_transition_label
        left_label += "|"

    right_label += prev_cur_state_transition_label
    if circular_transition_label is not None:
        if len(circular_transition_label) > 1:
            right_label += open_par
        right_label += circular_transition_label
        if len(circular_transition_label) > 1:
            right_label += ")"
        right_label += "*"
    if cur_next_state_transition_label != '':
        right_label += cur_next_state_transition_label

    if left_label != '':
        transition_label += open_par
    transition_label += left_label + right_label
    if left_label != '':
        transition_label += ")"

    return transition_label


def remove_state_from_transitions(transitions: TransitionsT, inverted_transitions: TransitionsT, state: str) -> Tuple[
    TransitionsT, TransitionsT]:
    new_transitions = dict()
    new_inverted_transitions = dict()
    for src_state in transitions:
        if src_state == state:
            continue
        new_dst_transitions = dict()
        for dst_state in transitions[src_state]:
            if dst_state == state:
                continue
            new_dst_transitions[dst_state] = transitions[src_state][dst_state]
        new_transitions[src_state] = new_dst_transitions

    for dst_state in transitions:
        if dst_state == state:
            continue
        new_src_transitions = dict()
        for src_state in inverted_transitions[dst_state]:
            if src_state == state:
                continue
            new_src_transitions[src_state] = inverted_transitions[dst_state][src_state]
        new_inverted_transitions[dst_state] = new_src_transitions

    return new_transitions, new_inverted_transitions


def reduce_state(fsm: FsmT, state: str) -> FsmT:
    (alphabet, states, initial_state, finals, transitions, inverted_transitions) = fsm
    prev_states: List[Tuple[str, str]] = []
    circular_letter = None
    next_states = []
    for prev_state in inverted_transitions[state]:
        if prev_state == state:
            circular_letter = inverted_transitions[state][prev_state]
        else:
            prev_states.append((prev_state, inverted_transitions[state][prev_state]))
    for next_state in transitions[state]:
        if next_state == state:
            circular_letter = transitions[state][next_state]
        else:
            next_states.append((next_state, transitions[state][next_state]))
    for prev_state_tuple in prev_states:
        for next_state_tuple in next_states:
            (prev_state, prev_letter) = prev_state_tuple
            (next_state, next_letter) = next_state_tuple
            prev_next_letter = transitions[prev_state].get(next_state)
            reduced_transition = create_reduced_transition(prev_letter, next_letter, prev_next_letter, circular_letter,
                                                           True)
            transitions[prev_state][next_state] = reduced_transition
            inverted_transitions[next_state][prev_state] = reduced_transition

    states.remove(state)
    (transitions, inverted_transitions) = remove_state_from_transitions(transitions, inverted_transitions, state)
    return alphabet, states, initial_state, finals, transitions, inverted_transitions


def compute_regex_from_fsm(fsm: FsmT) -> str:
    resulting_fsm = add_single_initial_state(fsm)
    resulting_fsm = add_single_final_state(resulting_fsm)
    (alphabet, states, initial_state, finals, transitions, inverted_transitions) = resulting_fsm
    final_state = list(finals)[0]
    initial_states = states.copy()
    for state in initial_states:
        if state != initial_state and state != final_state:
            resulting_fsm = reduce_state(resulting_fsm, state)
    (alphabet, states, initial_state, finals, transitions, inverted_transitions) = resulting_fsm
    final_state = list(finals)[0]
    return transitions[initial_state][final_state]