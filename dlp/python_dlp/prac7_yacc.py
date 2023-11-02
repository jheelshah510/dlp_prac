import ply.yacc as yacc

# Define the tokens
tokens = (
    'ID',
)

# Define the grammar rules
def p_S(p):
    '''
    S : 'i' E 't' S S_prime
      | 'a'
    '''

def p_S_prime(p):
    '''
    S_prime : 'e' S
            | empty
    '''

def p_E(p):
    '''
    E : 'b'
    '''

def p_empty(p):
    '''
    empty :
    '''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error")

# Build the parser
parser = yacc.yacc()

# Function to validate a string
def validate_string(input_string):
    try:
        parser.parse(input_string)
        print("String is valid.")
    except:
        print("String is not valid.")

# Example usage
input_string = "iaebtae"
validate_string(input_string)
