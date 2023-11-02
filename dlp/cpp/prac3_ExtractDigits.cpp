#include <iostream>
#include <string>
using namespace std;
int main() {
    string input_string = "Hello123World456";
    string digit_string = "";

    // Iterate through each character in the input string
    for (char character : input_string) {
        if (isdigit(character)) {
            digit_string += character;
        }
    }

   cout << "Extracted digits: " << digit_string << std::endl;

    return 0;
}
