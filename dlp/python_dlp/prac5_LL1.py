def compute_FIRST(grammar):
    FIRST = {}
    changed = True

    while changed:
        changed = False
        for nt in grammar:
            FIRST[nt] = set()
            for prod in grammar[nt]:
                for symbol in prod:
                    if symbol in grammar:
                        prev_len = len(FIRST[nt])
                        FIRST[nt] |= FIRST.get(symbol, set())
                        if len(FIRST[nt]) != prev_len:
                            changed = True
                        if '' not in FIRST.get(symbol, set()):
                            break
                    else:
                        prev_len = len(FIRST[nt])
                        FIRST[nt].add(symbol)
                        if len(FIRST[nt]) != prev_len:
                            changed = True
                        break

    return FIRST

def compute_FOLLOW(grammar, FIRST):
    FOLLOW = {nt: set() for nt in grammar}
    FOLLOW[list(grammar.keys())[0]].add('$')

    changed = True
    while changed:
        changed = False
        for nt in grammar:
            for prod in grammar[nt]:
                prev_set = set()
                for symbol in reversed(prod):
                    if symbol in grammar:
                        prev_len = len(FOLLOW[symbol])
                        FOLLOW[symbol] |= FOLLOW[nt]
                        if len(FOLLOW[symbol]) != prev_len:
                            changed = True
                        if '' not in FIRST.get(symbol, set()):
                            break
                    else:
                        prev_len = len(prev_set)
                        prev_set.add(symbol)
                        if len(prev_set) != prev_len:
                            changed = True
                for symbol in reversed(prod):
                    if symbol in grammar:
                        if '' not in FIRST.get(symbol, set()):
                            break

    return FOLLOW

def is_LL1(grammar):
    FIRST = compute_FIRST(grammar)
    FOLLOW = compute_FOLLOW(grammar, FIRST)

    for nt in grammar:
        productions = grammar[nt]
        first_sets = [FIRST[nt] for prod in productions]
        for i in range(len(first_sets)):
            for j in range(i + 1, len(first_sets)):
                if (first_sets[i] & first_sets[j]):
                    return False

        for prod in productions:
            if '' in FIRST[nt]:
                if (FIRST[nt] & FOLLOW[nt]):
                    return False

    return True

# Define the grammar using a dictionary
grammar = {
    'E': ['aX'],
    'X': ['+aX', 'c']
}

if is_LL1(grammar):
    print("The grammar is LL(1).")
else:
    print("The grammar is not LL(1).")
