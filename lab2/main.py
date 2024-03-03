import Grammar as g, FiniteAutomaton as fa
from automata.fa.nfa import NFA
from visual_automata.fa.nfa import VisualNFA

VN3_R = {'S', 'A', 'B', 'C'}
VT3_R = {'a', 'b'}
P3_R = {
    'S': ['aA'],
    'A': ['bS', 'aB'],
    'B': ['bC'],
    'C': ['aA', 'b']
    }

VN2 = {'S', 'A'}
VT2 = {'a', 'b', 'c', 'd'}
P2 = {
    'S': ['aS', 'bS', 'A', ''],
    'A': ['cA', 'd']
}

VN1 = {'S', 'X'}
VT1 = {'a', 'b'}
P1 = {
    'S': ['aXa', 'bXb'],
    'Xa': ['aX'],
    'Xb': ['bX'],
    'X ': [' ']
}

VN = ['S', 'A', 'B']
VT = {'a', 'b'}
P = {
    'S': ['aA', 'aS', 'bS'],
    'A': ['bB', 'bA'],
    'B': ['b', 'bB']
}

grammar = g.Grammar(VN, VT, P)
print(grammar.check_type())

finite_automaton = grammar.to_finite_automaton()
print(finite_automaton.is_nfa())
finite_automaton.draw()

