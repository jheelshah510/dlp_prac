# Function to convert infix expression to postfix expression
def infix_to_postfix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    postfix = []
    stack = []
    
    for token in infix.split():
        if token.isalnum():
            postfix.append(token)
        elif token in '+-*/':
            while stack and stack[-1] in '+-*/' and precedence[token] <= precedence[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
    
    while stack:
        postfix.append(stack.pop())
    
    return ' '.join(postfix)

# Function to generate the quadruple table
def generate_quadruple(postfix):
    stack = []
    quadruples = []
    temp_count = 1

    for token in postfix.split():
        if token.isalnum():
            stack.append(token)
        elif token in '+-*/':
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = 'T' + str(temp_count)
            temp_count += 1
            quadruples.append((token, operand1, operand2, result))
            stack.append(result)

    return quadruples

# Main program
infix_expression = input("Enter an infix expression: ")
postfix_expression = infix_to_postfix(infix_expression)
print("Postfix Expression:", postfix_expression)

quadruple_table = generate_quadruple(postfix_expression)
print("\nQuadruple Table:")
for index, quadruple in enumerate(quadruple_table, start=1):
    operator, op1, op2, result = quadruple
    print(f"{index}: ({operator}, {op1}, {op2}, {result})")
