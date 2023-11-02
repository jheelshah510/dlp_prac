#include <iostream>

void replaceInString(std::string &input, const std::string &target, const std::string &replacement) {
    size_t pos = input.find(target);
    while (pos != std::string::npos) {
        input.replace(pos, target.length(), replacement);
        pos = input.find(target, pos + replacement.length());
    }
}

int main() {
    std::string input_string = "I love USA. USA is a beautiful country. USA";

    replaceInString(input_string, "USA", "India");

    std::cout << "Modified string: " << input_string << std::endl;

    return 0;
}
