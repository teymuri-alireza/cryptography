from string import ascii_uppercase

def encrypt(plain_text: str, key_list: list) -> str:
    plain_text = plain_text.upper()
    plain_text = plain_text.replace(" ", "")
    # Remove duplicates from key_list, preserve order
    unique_set = set()
    key_unique = []
    for char in key_list:
        if char not in unique_set and char != "J":
            unique_set.add(char)
            key_unique.append(char)
    
    # Fill grid with key letters first
    grids = [[0 for _ in range(5)] for _ in range(5)]
    counter = 0
    for k in key_unique:
        grids[counter // 5][counter % 5] = k
        counter += 1
    # Fill remaining with A-Z, skipping J and key letters
    for char in ascii_uppercase:
        if char == "J" or char in unique_set:
            continue
        grids[counter // 5][counter % 5] = char
        counter += 1
        if counter >= 25:
            break
    
    

if __name__ == "__main__":
    plain_text = input("Enter text: \t")
    key = input("Enter key: \t")
    key_list = []
    for char in key:
        key_list.append(char.upper())
    cipher_text = encrypt(plain_text, key_list)
    print(f"Cipher text: \t{cipher_text}")