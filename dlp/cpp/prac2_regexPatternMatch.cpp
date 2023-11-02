#include <iostream>
#include <regex>

bool validateStringWithRegex(const std::string& regexPattern, const std::string& inputString) {
    try {
        std::regex regex(regexPattern);
        
        if (std::regex_match(inputString, regex) && inputString.length() == std::sregex_token_iterator(inputString.begin(), inputString.end(), regex, -1)->length()) {
            return true; // Valid
        } else {
            return false; // Invalid
        }
    } catch (const std::regex_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return false; // Invalid due to regex error
    }
}

int main() {
    std::string regexPattern = "^[A-Za-z0-9_]+$";  // Example regex: Allows only letters, digits, and underscores
    std::string inputString = "Hello123";
    
    bool isValid = validateStringWithRegex(regexPattern, inputString);
    
    if (isValid) {
        std::cout << "Valid" << std::endl;
    } else {
        std::cout << "Invalid" << std::endl;
    }

    return 0;
}
