def encrypt(plaintext: str, key: int) -> str:
    """
    Encrypts a given plaintext using the Rail Fence Cipher technique by arranging the characters in a zigzag pattern
    across a specified number of rails and then reading them row by row to produce the ciphertext.

    Args:
        plaintext (str): The plain text to be encrypted.
        key (int): The integer key for arranging characters.
    
    Returns:
        str: The cipher text.
    """
    plaintext = plaintext.replace(" ", "")
    # Create a list of empty strings for each rail
    rails = [''] * key

    rail = 0           # current rail
    direction = 1      # 1 = down, -1 = up

    for char in plaintext:
        rails[rail] += char
        rail += direction

        # Change direction at top or bottom rail
        if rail == 0 or rail == key - 1:
            direction *= -1

    # Join all rails
    return ''.join(rails)

def decrypt(ciphertext: str, key: int) -> str:
    """
    Decrypts a ciphertext encoded with the Rail Fence Cipher by reconstructing the zigzag rail pattern
    based on the given key, placing characters into their correct rail positions,
    and then reading them in zigzag order to recover the original plaintext.

    Args:
        ciphertext (str): The ciphertext encoded with the Rail Fence Cipher.
        key (int): The integer key for arranging characters.
    
    Returns:
        str: The decrypted original plaintext.
    """
    # Create a matrix to mark zigzag positions
    n = len(ciphertext)
    rail = [['' for _ in range(n)] for _ in range(key)]

    # Mark the pattern positions with '*'
    direction_down = None
    row, col = 0, 0
    for i in range(n):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    # Fill the marked spots with ciphertext characters
    index = 0
    for i in range(key):
        for j in range(n):
            if rail[i][j] == '*' and index < n:
                rail[i][j] = ciphertext[index]
                index += 1

    # Read the zigzag to reconstruct plaintext
    result = []
    row, col = 0, 0
    for i in range(n):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        result.append(rail[row][col])
        col += 1
        row += 1 if direction_down else -1

    return ''.join(result)

if __name__ == "__main__":
    plainText = "defend the east wall"
    key = 2
    cipherText = encrypt(plainText, key)
    recoverText = decrypt(cipherText, key)
    print("Original: \t", plainText)
    print("Enrypted: \t", cipherText)
    print("Decrypted: \t", recoverText)