#include <iostream>
#include <regex>
#include <string>

int main() {
    std::string input_string;
    std::regex pattern("0*1*(0|1)*1");

    std::cout << "Enter an input string: ";
    std::cin >> input_string;

    if (std::regex_match(input_string, pattern)) {
        std::cout << "The input string is valid." << std::endl;
    } else {
        std::cout << "The input string is invalid." << std::endl;
    }

    return 0;
}
