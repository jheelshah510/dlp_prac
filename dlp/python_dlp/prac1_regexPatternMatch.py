import re

def validate_string_with_regex(regex, input_string):
    try:
        # Attempt to compile the provided regular expression
        compiled_regex = re.compile(regex)
        
        # Use the compiled regex to match against the input string
        match = compiled_regex.match(input_string)
        
        # If there is a match, and it spans the entire string, it's valid
        if match and match.span() == (0, len(input_string)):
            return "Valid"
        else:
            return "Invalid"
    except re.error as e:
        # If there's an issue with the provided regex, return an error message
        return "Error: " + str(e)

# Example usage:
regular_expression = r'^[A-Za-z0-9_]+$'  # Example regex: Allows only letters, digits, and underscores
input_string = "Hello123"

result = validate_string_with_regex(regular_expression, input_string)
print(result)
