"""
Variant 19:
VN={S, A, B, C},
VT={a, b},
P={
    S → aA
    A → bS
    A → aB
    B → bC
    C → aA
    C → b
}
"""
import random


class Grammar:
    def __init__(self):
        self.VN = {'S', 'A', 'B', 'C'}
        self.VT = {'a', 'b'}
        self.P = {
            'S': ['aA'],
            'A': ['bS', 'aB'],
            'B': ['bC'],
            'C': ['aA', 'b']
        }
    def generate_string(self, symbol='S', current_string=''):
        if symbol == '':
            return current_string
        symbols = random.choice(self.P[symbol])
        if current_string == '':
            current_string += symbols
        for char in current_string:
            if char in self.VN:
                current_string = current_string.replace(char, random.choice(self.P[char]))
                result = self.generate_string(symbol=char, current_string=current_string)
                return result
        return self.generate_string(symbol='', current_string=current_string)

    def generate_strings(self):
        arr = []
        for i in range(5):
            arr.append(self.generate_string())
        return arr

    def to_finite_automaton(self):
        states = self.VN
        alphabet = self.VT
        initial_state = 'S'
        transitions = {}
        final_states = []

        for state, productions in self.P.items():
            for production in productions:
                arr = [state]
                for symbol in production:
                    if symbol in self.VT:
                        arr.append(symbol)
                        if len(production) == 1:
                            final_states.append(production)
                            transitions[tuple(arr)] = production
                    elif symbol in self.VN:
                        transitions[tuple(arr)] = symbol
        return FiniteAutomaton(states, alphabet, transitions, initial_state, set(final_states))


class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.Q = states
        self.sigma = alphabet
        self.δ = transitions
        self.q0 = initial_state
        self.current_state = initial_state
        self.F = final_states
        #print(f'{states}\n {alphabet}\n {transitions}\n {initial_state}\n {final_states}')

    def transition(self, symbol):
        if (self.current_state, symbol) in self.δ:
            self.current_state = self.δ[(self.current_state, symbol)]
            return True
        else:
            return False

    def reset(self):
        self.current_state = self.q0

    def is_string_accepted(self, input_string):
        for symbol in input_string:
            if symbol not in self.sigma or not self.transition(symbol):
                return False
        return self.current_state in self.F


grammar = Grammar()
strings = grammar.generate_strings()
print(strings)
strings.append('aabaabba')
strings.append('aabab')

finite_automaton = grammar.to_finite_automaton()

for string in strings:
    finite_automaton.reset()
    if finite_automaton.is_string_accepted(string):
        print(f'String "{string}" is accepted by the Finite Automaton')
    else:
        print(f'String "{string}" is not accepted by the Finite Automaton')
