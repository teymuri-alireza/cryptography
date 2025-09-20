def vigerene_encrypt(text: str, key: str):
    """
    Encrypts plain text with given key using vigerene cipher algorithm.
    Note that all the letters should be upper-case.

    Args:
        text (str): plain text
        key (str): the key

    Returns:
        str: The encrypted text in upper-case
    """
    input = text.upper()
    key_upper = key.upper()
    cipher_text = ""
    key_length = len(key)
    key_index = 0

    for ch in input:
        if ch.isalpha():
            base = ord("A")
            # This part makes sure the key repeats itself
            shift = ord(key_upper[key_index % key_length]) - base
            # turning the integer shifted to character
            cipher_char = chr((ord(ch) + shift - base) % 26 + base)
            cipher_text += cipher_char
            # going though key characters
            key_index += 1
        else:
            cipher_text += ch

    return cipher_text


def vigerene_decrypt(text: str, key: str):
    """
    Decrypts cipher text with given key using vigerene cipher algorithm.
    Note that all the letters should be upper-case.

    Args:
        text (str): cipher text
        key (str): the key

    Returns:
        str: The decrypted text in upper-case
    """
    input = text.upper()
    key_upper = key.upper()
    plain_text = ""
    key_length = len(key)
    key_index = 0

    for ch in input:
        if ch.isalpha():
            base = ord("A")
            # This part makes sure the key repeats itself
            shift = ord(key_upper[key_index % key_length]) - base
            # turning the integer shifted to character
            plain_char = chr((ord(ch) - shift - base + 26) % 26 + base)
            plain_text += plain_char
            # going though key characters
            key_index += 1
        else:
            plain_text += ch

    return plain_text


if __name__ == "__main__":
    try:
        text = input("Enter text: ")
        key = input("Enter key: ")
        encrypted_text = vigerene_encrypt(text, key)
        decrypted_text = vigerene_decrypt(encrypted_text, key)
        print()
        print("Encrypted text: ", encrypted_text)
        print("decrypted text: ", decrypted_text)
    except Exception:
        print("Error occured")
