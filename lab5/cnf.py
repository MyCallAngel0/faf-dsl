import variants
class Grammar:
    def __init__(self, Vn: set, Vt: set, P: dict):
        self.Vn = Vn
        self.Vt = Vt
        self.P = P

    def check_empty(self):
        states_to_remove = set()
        for key, value in self.P.items():
            if len(value) == 0:
                empty_state = key
                states_to_remove.add(key)
                for state, productions in self.P.items():
                    change = False
                    for production in productions:
                        if empty_state in production:
                            if len(production) == 1:
                                productions.remove(production)
                            else:
                                productions[productions.index(production)] = production.replace(empty_state, "")
                                change = True
                    if change:
                        self.P[state] = list(set(productions))

        for state in states_to_remove:
            if state in self.P.keys():
                self.P.pop(state)
                self.Vn.remove(state)

    def eliminate_state(self, production, state):
        new_productions = [production]
        for c in new_productions:
            if state in c:
                if sum(char == state for char in c) > 1:
                    str = c[:c.rfind(state)] + c[c.rfind(state) + 1:]
                    if str not in new_productions:
                        new_productions.append(str)
                str = c[:c.index(state)] + c[c.index(state) + 1:]
                if str not in new_productions:
                    new_productions.append(str)
        new_productions.remove(production)
        return new_productions

    def eliminate_epsilon(self):
        epsilon_state = ''
        for state, productions in self.P.items():
            if '' in productions:
                epsilon_state = state
                productions.remove('')
                for key, value in self.P.items():
                    new_productions = []
                    for production in value:
                        if epsilon_state in production and len(production) > 1:
                                new_productions += self.eliminate_state(production, epsilon_state)
                    value += new_productions
        # print(self.P)
        self.check_empty()
        print(self.P)
        return self.P

    def eliminate_unit(self):
        unit_productions = {}
        for state, productions in self.P.items():
            for production in productions:
                if len(production) == 1 and production[0].isupper():
                    productions.remove(production)
                    unit_productions.setdefault(state, []).append(production)

        if not bool(unit_productions):
            return

        for state in self.P.keys():
            if state in unit_productions.keys():
                for unit in unit_productions[state]:
                    self.P[state].extend(self.P[unit])
                    self.P[state] = list(set(self.P[state]))

        self.check_empty()
        # print(self.P)
        return self.P

    def eliminate_inaccessible(self):
        reachable_symbols = set()  # Set to store reachable symbols
        pending_symbols = [list(self.P.keys())[0]]  # Start with the start symbol

        while pending_symbols:
            symbol = pending_symbols.pop(0)
            reachable_symbols.add(symbol)
            for production in self.P[symbol]:
                for char in production:
                    if char.isupper() and char not in reachable_symbols:
                        pending_symbols.append(char)

        # Remove unreachable symbols from the grammar
        unreachable_symbols = set(self.P.keys()) - reachable_symbols
        for symbol in unreachable_symbols:
            del self.P[symbol]
            self.Vn.remove(symbol)

        # Remove productions containing unreachable symbols
        for symbol, productions in self.P.items():
            self.P[symbol] = [prod for prod in productions if all(char not in unreachable_symbols for char in prod)]
        # print(self.P)
        self.check_empty()

    def eliminate_non_productive(self):
        productive_symbols = set()
        changed = True
        while changed:
            changed = False
            for symbol, productions in self.P.items():
                if symbol in productive_symbols:
                    continue
                if any(len(production) == 1 and production.islower() for production in self.P[symbol]):
                    productive_symbols.update(symbol)
                    changed = True
                    continue
                non_terminals = set()
                for prod in self.P[symbol]:
                    non_terminals.update(char for strings in prod for char in strings if (char.isupper() and char != symbol))
                if all(non_terminal in productive_symbols for non_terminal in non_terminals):
                    productive_symbols.update(symbol)
                    changed = True

        if len(productive_symbols) != len(self.Vn):
            raise Exception("Not all symbols are productive")

    def to_cnf(self):
        self.eliminate_epsilon()
        self.eliminate_unit()
        self.eliminate_inaccessible()
        self.eliminate_non_productive()
        print(self.P)
        new_productions = {}
        symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for state, productions in self.P.items():
            # print("\nKey:", state)
            new_strings = []
            for prod in productions:
                # print(prod)
                if len(prod) != 1 and not(len(prod) == 2 and prod[0].isupper() and prod[1].isupper()):
                    for n in range(len(prod)):
                        if prod[n].islower():
                            assigned_key = next((key for key, array in new_productions.items() if prod[n] in array), None)
                            if assigned_key is None:
                                while symbols[0] in self.Vn:
                                    symbols = symbols.replace(symbols[0], '')
                                symbol = symbols[0]
                                self.Vn.add(symbol)
                                # print("Symbol:", symbol)
                                new_productions[symbol] = list(prod[n])
                            else:
                                symbol = assigned_key
                            prod = prod[:n] + symbol + prod[n + 1:]
                            # print("New prod:", prod)
                    while len(prod) > 2:
                        assigned_key = next((key for key, array in new_productions.items() if prod[0] + prod[1] in array), None)
                        if assigned_key is None:
                            while symbols[0] in Vn:
                                symbols = symbols.replace(symbols[0], '')
                            symbol = symbols[0]
                            Vn.add(symbol)
                            # print("Symbol:", symbol)
                            str = prod[0] + prod[1]
                            new_productions[symbol] = [str]
                        else:
                            symbol = assigned_key
                        prod = prod.replace(prod[0] + prod[1], symbol)
                        # print("New prod:", prod)
                new_strings.append(prod)
            self.P[state] = new_strings

        self.P.update(new_productions)

    def print_grammar(self):
        print("P = {")
        for key, value in self.P.items():
            print("\t", key, "->", end=" ")
            for prod in value:
                if value.index(prod) != len(value) - 1:
                    print(prod, end=" | ")
                else:
                    print(prod)
        print("}")


if __name__ == "__main__":
    Vn = {'S', 'A', 'B', 'C', 'E'}
    Vt = {'a', 'd'}
    P = {
        'S': ['dB', 'B'],
        'A': ['d', 'S', 'aAdCB'],
        'B': ['aC', 'bA', 'AC'],
        'C': [''],
        'E': ['AS']
    }

    # grammar = Grammar(Vn, Vt, P)
    grammar = Grammar(variants.Vn1, variants.Vt1, variants.P1)
    grammar.to_cnf()
    grammar.print_grammar()
    print(Grammar(variants.Vn2, variants.Vt2, variants.P2).eliminate_unit())

