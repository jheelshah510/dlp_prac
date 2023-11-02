#include <iostream>
#include <string>

class Parser {
public:
    bool parseE(std::string& input) {
        if (input.empty()) {
            return false;
        }
        if (input[0] == 'a') {
            input.erase(0, 1);  // Consume 'a'
            return parseX(input);
        }
        return false;
    }

    bool parseX(std::string& input) {
        if (input.empty()) {
            return false;
        }
        if (input[0] == 'c') {
            input.erase(0, 1);  // Consume 'c'
            return true;
        } else if (input[0] == '+') {
            input.erase(0, 1);  // Consume '+'
            if (input[0] == 'a') {
                input.erase(0, 1);  // Consume 'a'
                return parseX(input);
            }
        }
        return false;
    }
};

int main() {
    Parser parser;
    std::string input;

    std::cout << "Enter an input string: ";
    std::cin >> input;

    if (parser.parseE(input) && input.empty()) {
        std::cout << "Valid string" << std::endl;
    } else {
        std::cout << "Invalid string" << std::endl;
    }

    return 0;
}
