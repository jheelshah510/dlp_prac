#include <iostream>
#include <string>

int main() {
    std::string input_string = "My name is Jheel. Jheel is a common name. My friend's name is Jheel.";

    std::string name_to_count = "Jheel";

    size_t pos = 0;
    size_t count = 0;

    while ((pos = input_string.find(name_to_count, pos)) != std::string::npos) {
        count++;
        pos += name_to_count.length();
    }

    std::cout << "Occurrences of your name (" << name_to_count << "): " << count << std::endl;

    return 0;
}
