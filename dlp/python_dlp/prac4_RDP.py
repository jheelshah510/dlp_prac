class Parser:
    def __init__(self, input_string):
        self.input = input_string

    def parseE(self):
        if self.input and self.input[0] == 'a':
            self.input = self.input[1:]  # Consume 'a'
            return self.parseX()
        return False

    def parseX(self):
        if not self.input:
            return False
        if self.input[0] == 'c':
            self.input = self.input[1:]  # Consume 'c'
            return True
        elif self.input[0] == '+':
            self.input = self.input[1:]  # Consume '+'
            if self.input and self.input[0] == 'a':
                self.input = self.input[1:]  # Consume 'a'
                return self.parseX()
        return False

def main():
    input_string = input("Enter an input string: ")
    parser = Parser(input_string)

    if parser.parseE() and not parser.input:
        print("Valid string")
    else:
        print("Invalid string")

if __name__ == "__main__":
    main()
