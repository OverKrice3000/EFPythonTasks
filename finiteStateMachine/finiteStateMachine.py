from typing import Optional

from typings import AlphabetT, FinalsT, InitialT, StatesT, TransitionsT


class FiniteStateMachine:
    __alphabet: AlphabetT
    __states: StatesT
    __initial_state: Optional[InitialT]
    __final_states: FinalsT
    __transitions: TransitionsT
    __inverted_transitions: TransitionsT

    def __init__(self, alphabet: AlphabetT):
        self.__alphabet = alphabet
        self.__states = []
        self.__initial_state = None
        self.__final_states = set()
        self.__transitions = {}
        self.__inverted_transitions = {}

    def add_state(self, state: str):
        if state in self.__states:
            return
        self.__states.append(state)

    def remove_state(self, state: str):
        for current_state in self.__states:
            self.__remove_direct_transition(current_state, state)
            self.__remove_reversed_transition(state, current_state)
        self.__transitions.pop(state)
        self.__inverted_transitions.pop(state)

    def set_initial(self, state: str):
        if state not in self.__states:
            return
        self.__initial_state = state

    def set_final(self, state: str):
        if state not in self.__states:
            return
        self.__final_states.add(state)

    def remove_final(self, state: str):
        if state not in self.__final_states:
            return
        self.__final_states.remove(state)

    def add_transition(self, first: str, second: str, symbol: str):
        if first not in self.__states or second not in self.__states:
            return
        self.__add_direct_transition(first, second, symbol)
        self.__add_reversed_transition(first, second, symbol)

    def __add_direct_transition(self, first: str, second: str, symbol: str):
        if self.__transitions.get(first) is None:
            self.__transitions[first] = {
                second: symbol
            }
        else:
            self.__transitions[first][second] = symbol

    def __add_reversed_transition(self, first: str, second: str, symbol: str):
        if self.__inverted_transitions.get(second) is None:
            self.__transitions[second] = {
                first: symbol
            }
        else:
            self.__transitions[second][first] = symbol

    def remove_transition(self, first: str, second: str):
        self.__remove_direct_transition(first, second)
        self.__remove_reversed_transition(first, second)

    def __remove_direct_transition(self, first: str, second: str):
        if self.__transitions.get(first) is None:
            return
        self.__transitions[first].pop(second)

    def __remove_reversed_transition(self, first: str, second: str):
        if self.__inverted_transitions.get(second) is None:
            return
        self.__inverted_transitions[second].pop(first)

    def clear(self):
        self.__states = []
        self.__initial_state = None
        self.__final_states = set()
        self.__transitions = {}
        self.__inverted_transitions = {}

    def test(self, string: str):
        if self.__initial_state is None:
            return
        current_state = self.__initial_state
        for char in string:
            state_dict = self.__transitions[current_state]
            next_state = None
            for (key, value) in state_dict.items():
                if value == char:
                    next_state = key
            if next_state is None:
                return False
            current_state = next_state
        return current_state in self.__final_states

