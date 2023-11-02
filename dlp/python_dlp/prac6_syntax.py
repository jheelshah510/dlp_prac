def syntax_check(input_string, ll1_table, start_symbol):
    stack = []
    stack.append('$')  # Initialize stack with end-of-input marker
    stack.append(start_symbol)  # Push the start symbol onto the stack
    input_index = 0  # Initialize input index to point to the first character of the input

    print("Parsing Steps:")

    while len(stack) > 0:
        # Current symbol at the top of the stack
        top_of_stack = stack[-1]

        if top_of_stack in ll1_table:
            # Non-terminal symbol at the top of the stack
            if (top_of_stack, input_string[input_index]) in ll1_table[top_of_stack]:
                production = ll1_table[top_of_stack][(top_of_stack, input_string[input_index])]
                print(f"Using production: {top_of_stack} -> {' '.join(production)}")

                # Pop the non-terminal from the stack
                stack.pop()

                # Push the production onto the stack in reverse order
                for symbol in reversed(production):
                    if symbol != '':
                        stack.append(symbol)
            else:
                print("Syntax Error: Invalid input.")
                return False
        elif top_of_stack == input_string[input_index]:
            # Terminal symbol at the top of the stack matches the input
            print(f"Matched: {input_string[input_index]}")
            stack.pop()
            input_index += 1
        elif top_of_stack == '$' and input_string[input_index] == '$':
            # Successfully parsed the input
            print("Input string is syntactically correct.")
            return True
        else:
            print("Syntax Error: Invalid input.")
            return False

    return False  # If the stack is empty and parsing is not successful

# Example LL(1) parsing table (replace with your LL(1) table)
ll1_table = {
    'E': {('E', 'a'): ['T', "E'"]},
    "E'": {('+', 'a'): ['+', 'T', "E'"], '$': ['']},
    'T': {('T', 'a'): ['F', "T'"]},
    "T'": {('*', 'a'): ['*', 'F', "T'"], '+': [''], '$': ['']},
    'F': {('(', 'a'): ['(', 'E', ')'], 'a': ['a']}
}

# Input string to check (modify as needed)
input_string = "a+a*a"

# Start symbol of the grammar
start_symbol = 'E'

# Perform syntax check
syntax_check(input_string, ll1_table, start_symbol)
