class DownwardPattern:
    """
    In downward pattern we fill rows left→right, then read columns top→bottom.
    There is no column order and it's the simplest emthod.

    If we used a column order, it'll become Columnar cipher!
    """
    def encrypt(self, plain_text: str, column_key: int, pad_char = ".") -> str:
        plain_text = plain_text.replace(" ", "")
        while len(plain_text) % column_key != 0:
            plain_text += pad_char
        grids = [""] * column_key
        i = 0
        while i < len(plain_text):
            current_column = i % column_key
            grids[current_column] += plain_text[i]
            i += 1
        return "".join(grids)

    def decrypt(self, cipher_text: str, column_key: int) -> str:
        if len(cipher_text) % column_key == 0:
            rows = len(cipher_text) // column_key
        else:
            rows = ( len(cipher_text) // column_key ) + 1
        grids = [""] * rows
        i = 0
        while i < len(cipher_text):
            current_column = i % rows
            grids[current_column] += cipher_text[i]
            i += 1
        return "".join(grids)


if __name__ == "__main__":
    plain_text = input("Enter text for encrypting: \t\t")
    try:
        column_key = int(input("Enter number of columns for grid: \t"))
    except ValueError:
        print("Invalid column number.")
        exit()
    method = input("""Choose a method:
1. Downward Pattern
(more patterns will be added later)
""")
    if method == "1":
        instance = DownwardPattern()
        cipher_text = instance.encrypt(plain_text, column_key)
        recover_text = instance.decrypt(cipher_text, column_key)
        print(f"Original text: \t\t{plain_text}")
        print(f"Cipher text: \t\t{cipher_text}")
        print(f"Decrypted text: \t{recover_text}")
    else:
        print("wrong method. exiting...")