#include <iostream>
#include <string>

std::string encrypt(std::string text, int key);
std::string dencrypt(std::string text, int key);

int main() {
    // ensures the program can handle UTF-8 characters properly
    std::locale::global(std::locale("en_US.UTF-8"));
    std::string input;
    int key;
    std::cout << "Enter input: ";
    getline(std::cin, input);
    std::cout << "Enter key: ";
    std::cin >> key;
    std::string encrypt_input = encrypt(input, key);
    std::string decrypt_input = dencrypt(encrypt_input, key);
    std::cout << "Encrypted text: " << encrypt_input << "\n";
    std::cout << "Decrypted text: " << decrypt_input << "\n";
    return 0;
}

std::string encrypt(std::string text, int key) {
    std::string cipher_text = "";
    for (char ch: text) {
        // checks if the character is a letter
        if (isalpha(ch)) {
            // sets the ASCII base depending on uppercase or lowercase
            int base = isupper(ch) ? int('A') : int('a');
            // shifts the letter by key positions in the alphabet
            char shifted = char((int(ch) - base + key) %26 + base);
            cipher_text += shifted;
        } else {
            // Non-letter characters are left unchanged
            cipher_text += ch;
        }
    }
    return cipher_text;
}

std::string dencrypt(std::string text, int key) {
    // To decrypt, it simply calls encrypt() again with the negative of the key.
    //This works because reversing a Caesar cipher is just shifting in the opposite direction.
    int negetive_key = -1 * key;
    std::string decrypted = encrypt(text, negetive_key);
    return decrypted;
}