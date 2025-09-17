def caesar_encrypt(text: str, key:int = 3) -> str:
    """
    Encrypts a string using the Caesar cipher.

    Each letter in the input text is shifted forward in the alphabet by 
    the specified key. Non-alphabetic characters are left unchanged. 
    The case of letters is preserved.

    Args:
        text (str): The plaintext string to be encrypted.
        key (int): The number of positions to shift each letter (can be positive).

    Returns:
        str: The encrypted ciphertext.
    """
    cipher_text = ""
    for ch in text:
        if ch.isalpha():
            # Determine ASCII base depending on uppercase or lowercase
            base = ord("A") if ch.isupper() else ord("a")
            # Shift letter by key within 0-25 range and convert back to ASCII
            shifted = (ord(ch) - base + key) % 26 + base
            cipher_text += chr(shifted)
        else:
            # Non-alphabetic characters are added unchanged
            cipher_text += ch
    return cipher_text

def caesar_decrypt(text:str, key:int = 3) -> str:
    """
    Decrypts a string encrypted with the Caesar cipher.

    This function reverses the Caesar cipher by calling `caesar_encrypt` 
    with the negative of the provided key, effectively shifting letters 
    back to their original positions. Non-alphabetic characters remain unchanged.

    Args:
        text (str): The ciphertext string to be decrypted.
        key (int): The number of positions used to shift each letter during encryption.

    Returns:
        str: The decrypted plaintext.
    """
    negative_key = -1 * key
    return caesar_encrypt(text=text, key=negative_key)

if __name__ == "__main__":
    try:
        text = input("Enter your text: ")
        key = input("Enter Value for key [default: 3]: ")
        key = int(key) if key.strip() else 3

        encrypted = caesar_encrypt(text, key)
        decrypted = caesar_decrypt(encrypted, key)
        
        print() # empty line for better readability
        print("original text: ", text)
        print("encrypted text: ", encrypted)
        print("dencrypted text: ", decrypted)
    except:
        print("Error occured")