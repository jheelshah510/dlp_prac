#include <iostream>
#include <string>
#include <cctype>

int main() {
    std::string input_string = "Hello123World456";
    std::string number = "";
    bool inNumber = false;

    for (char character : input_string) {
        if (std::isdigit(character)) {
            number += character;
            inNumber = true;
        } else if (inNumber) {
            // Print the extracted number and reset
            std::cout << "Extracted number: " << number << std::endl;
            number = "";
            inNumber = false;
        }
    }

    // If there is a number at the end of the string, print it
    if (inNumber) {
        std::cout << "Extracted number: " << number << std::endl;
    }

    return 0;
}
