import Grammar as g
from collections import deque
from automata.fa.nfa import NFA
from visual_automata.fa.nfa import VisualNFA


class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.Q = states
        self.Σ = alphabet
        self.δ = transitions
        self.q0 = initial_state
        self.current_state = initial_state
        self.F = final_states
        print(f'states={states}\nalphabet={alphabet}\ntransitions={transitions}\ninitial_state={initial_state}\nfinal_state={final_states}')

    def transition(self, symbol):
        if (self.current_state, symbol) in self.δ:
            self.current_state = self.δ[(self.current_state, symbol)]
            return True
        else:
            return False

    def reset(self):
        self.current_state = self.q0

    # deprecated
    def is_string_accepted_old(self, input_string):
        for symbol in input_string:
            if symbol not in self.Σ or not self.transition(symbol):
                return False
        return self.current_state in self.F

    def is_nfa(self) -> bool:
        return any(len(production) > 1 for production in self.δ.values())

    def to_grammar(self):
        VN = list(self.Q)
        VT = self.Σ
        P = {}
        for key in self.δ.keys():
            if key[0] not in P.keys():
                P[key[0]] = []
            for symbol in self.δ[key]:
                if symbol == key[1]:
                    production = symbol
                else:
                    production = key[1] + symbol
                P[key[0]].append(production)
        return g.Grammar(VN, VT, P)

    def draw(self):
        states = self.Q
        alphabet = self.Σ
        initial_state = self.q0
        transitions = {}
        my_transitions = self.δ
        for key in my_transitions.keys():
            my_transitions[key] = {element for element in my_transitions[key] if not element.islower()}
            new_transition = {}
            if self.is_nfa():
                new_transition[key[1]] = my_transitions[key]
            else:
                new_transition[key[1]] = list(my_transitions[key])[0]
            if key[0] in transitions.keys():
                transitions[key[0]].update(new_transition)
            else:
                transitions[key[0]] = new_transition
        show_nfa = VisualNFA(states=self.Q, input_symbols=self.Σ, transitions=transitions, initial_state=self.q0, final_states=self.F)
        print(show_nfa.table)
        show_nfa.show_diagram()

"""
Variant 19
Q = {q0,q1,q2},
∑ = {a,b},
F = {q2},
δ(q0,a) = q1,
δ(q0,a) = q0,
δ(q1,b) = q2,
δ(q0,b) = q0,
δ(q1,b) = q1,
δ(q2,b) = q2.  
"""

