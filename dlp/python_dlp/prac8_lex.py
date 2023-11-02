from ply import lex

# Define the token names
tokens = (
    'ID',
    'INTEGER',
)

# Define regular expressions for the token names
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_INTEGER = r'\d+'

# Create a symbol table
symbol_table = set()

# Define a function to add an identifier to the symbol table
def add_to_symbol_table(t):
    symbol_table.add(t.value)

# Define an error handling function
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Input string for lexical analysis
input_string = "x = 42 y = abc123"

lexer.input(input_string)

# Perform lexical analysis
for tok in lexer:
    if tok.type == 'ID':
        add_to_symbol_table(tok)

# Print the symbol table
print("Symbol Table:")
for identifier in symbol_table:
    print(identifier)
