import random, FiniteAutomaton as fa

class Grammar:
    def __init__(self, VN, VT, P):
        self.VN = VN
        self.VT = VT
        self.P = P
        print(f'VN={self.VN}\nVT={self.VT}\nP={self.P}')
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

    def check_type(self):
        if all(string in (set(self.VN) | self.VT) and key in self.VN for key, array in self.P.items() for string in array):
            return "Grammar is not valid"
        value = "Type 0 - Recursively Enumerable Grammar"
        if all((len(string) == 2 and string[0] in self.VT and string[1] in self.VN) or
               (len(string) == 1 and string in self.VT) for array in self.P.values() for string in array):
            return "Type 3 - Right Regular Grammar"
        elif all((len(string) == 2 and string[0] in self.VN and string[1] in self.VT) or
                 (len(string) == 1 and string in self.VT) for array in self.P.values() for string in array):
            return "Type 3 - Left Regular Grammar"
        if any((sum(symbol in self.VN for symbol in string) > 1 or len(string) > 2
                  or sum(symbol in self.VT for symbol in string) > 1 or string == '')
                    for array in self.P.values() for string in array):
            value = "Type 2 - Context-Free Grammar"
        if (any(len(state) > 1 for state in self.P.keys()) and
                all(len(state.strip()) <= len(string) for state in self.P.keys() for string in self.P[state])):
            value = "Type 1 - Context-Sensitive Grammar"
        return value

    def to_finite_automaton(self):
        states = set(self.VN)
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
                        if tuple(arr) not in transitions.keys():
                            transitions[tuple(arr)] = set()
                        if len(production) == 1:
                            final_states.append(state)
                            transitions[tuple(arr)].add(production)
                    elif symbol in self.VN:
                        transitions[tuple(arr)].add(symbol)
        return fa.FiniteAutomaton(states, alphabet, transitions, initial_state, set(final_states))

    def convert_grammar_to_nfa(self):
        grammar_states = self.VN
        states = set()
        alphabet = self.VT
        transitions = {}
        start_state = 'q0'
        accept_states = set()

        states.add(start_state)
        for non_terminal in self.VN:
            states.add(non_terminal)

        for non_terminal, productions in self.P.items():
            for production in productions:
                current_state = start_state
                for symbol in production:
                    if symbol in self.VT:
                        next_state = 'q' + str(len(states))
                        states.add(next_state)
                        transitions.setdefault((current_state, symbol), []).append(next_state)
                        current_state = next_state
                if current_state not in accept_states:
                    accept_states.add(current_state)

        return fa.FiniteAutomaton(states, alphabet, transitions, start_state, accept_states)