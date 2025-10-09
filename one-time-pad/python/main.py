import secrets, base64

def xor_bytes(a: bytes, b: bytes) -> bytes:
    """
    Performs a byte-wise XOR operation
    """
    return bytes(x ^ y for x, y in zip(a, b))

def encrypt_otp(plaintext: str, key: bytes) -> str:
    """
    Encrypts the given plaintext using a One-Time Pad (OTP) approach.
    
    Steps:
    1. Convert the plaintext into UTF-8 encoded bytes.
    2. Verify the length of text and the key. (a strict requirement for OTP security)
    3. Apply xor_bytes function for XOR operation.
    4. Encode the ciphertext into base64 to ensure it is printable and easy to store or transmit.
    
    Returns:
        str: A Base64-encoded string representing the ciphertext.
    """
    b_plain = plaintext.encode("utf-8")
    if len(key) != len(b_plain):
        raise ValueError("For OTP, key and text must have the same size!")
    cipher = xor_bytes(b_plain, key)
    return base64.b64encode(cipher).decode("ascii")

def decrypt_otp(cipher_64: str, key: bytes) -> str:
    """
    Decrypts a Base64-encoded ciphertext that was encrypted using a One-Time Pad (OTP).

    Steps:
    1. Decode the Base64-encoded ciphertext to retrieve the original byte sequence.
    2. Verify the length of text and the key.
    3. Apply the XOR operation.
    4. Decode the plaintext bytes into a UTF-8 string.

    Returns:
        str: The original plaintext string.
    """
    cipher = base64.b64decode(cipher_64.encode("ascii"))
    if len(key) != len(cipher):
        raise ValueError("The key and cipher text lengths are not the same!")
    plain = xor_bytes(cipher, key)
    return plain.decode('utf-8')

if __name__ == "__main__":
    plaintext = "Hello World!"
    # generating secure key as long as the text
    key = secrets.token_bytes(len(plaintext.encode('utf-8')))

    cipher_b64 = encrypt_otp(plaintext, key)
    recovered = decrypt_otp(cipher_b64, key)

    print("Plaintext:\t\t", plaintext)
    print("Cipher (base64):\t", cipher_b64)
    # store key in a secure place
    print("Key:\t\t\t", key.hex())
    print("Recovered:\t\t", recovered)
