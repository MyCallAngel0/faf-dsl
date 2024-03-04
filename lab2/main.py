import Grammar as g, FiniteAutomaton as fa

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

grammar = g.Grammar(VN3_R, VT3_R, P3_R)
print(grammar.check_type())
print()
states = {'q1', 'q0', 'q2'}
alphabet = {'a', 'b'}
transitions = {('q0', 'a'): {'q1', 'q0'}, ('q0', 'b'): {'q0'}, ('q1', 'b'): {'q1', 'q2'}, ('q2', 'b'): {'b', 'q1'}}
initial_state = 'q0'
final_state = {'q2'}
fa = fa.FiniteAutomaton(states, alphabet, transitions, initial_state, final_state)
print()
print("Is the finite automaton NFA?:", fa.is_nfa())
print()
grammar = fa.to_grammar()
print()
fa.draw()

