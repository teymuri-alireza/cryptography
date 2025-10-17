from string import ascii_uppercase
import numpy as np

def check_indexes(first_place, second_place):
    # First_place and second_place come from np.argwhere -> arrays like [[i, j]]
    i, j = map(int, first_place[0])
    m, n = map(int, second_place[0])

    # Same row: replace each letter with the one to the right (wrap around)
    if i == m and j != n:
        return [[i, (j + 1) % 5], [m, (n + 1) % 5]]
    # Same column: replace each letter with the one below (wrap around)
    elif j == n and i != m:
        return [[(i + 1) % 5, j], [(m + 1) % 5, n]]
    # Rectangle: swap columns
    elif i != m and j != n:
        return [[i, n], [m, j]]
    # Identical positions (shouldn't happen after digraph prep) -> return as-is
    return [[i, j], [m, n]]


def encrypt(plain_text: str, key_list: list) -> str:
    # --- The grid part ---
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
    # --- The encryption part ---
    # Add null character after repeated characters
    new_plain = ""
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        b = plain_text[i+1] if i+1 < len(plain_text) else ""
        if b == "":
            # Using null character "X" to make length even
            new_plain += a + "X"
            i += 1
        elif a == b:
            # repeated pair
            new_plain += a + "X"
            i += 1
        else:
            # normal pair
            new_plain += a + b
            i += 2
    plain_text = new_plain

    # Every 2 characters in a plain_text is called a digraph
    digraphs = list()
    i = 0 
    while i < len(plain_text):
        temp_data = plain_text[i] + plain_text[i+1]
        digraphs.append(temp_data)
        i += 2

    result = ""
    numpy_grid = np.array(grids)
    for group in digraphs:
        first_letter = group[0]
        second_letter = group[1]
        # Finding digraph character's index in grid
        first_place, second_place = np.argwhere(numpy_grid == first_letter), np.argwhere(numpy_grid == second_letter)
        # Make chnages and encrypt for indexes
        cipher_indexes = check_indexes(first_place, second_place)
        # Appending the encrypted character into final result
        for index_counter2 in range(len(cipher_indexes)):
            result += numpy_grid[tuple(cipher_indexes[index_counter2])]

    return numpy_grid, result


if __name__ == "__main__":
    plain_text = input("Enter text: \t")
    key = input("Enter key: \t")
    key_list = []
    for char in key:
        key_list.append(char.upper())
    grid ,cipher_text = encrypt(plain_text, key_list)
    print(f"Grid:\n{grid}")
    print(f"\nOriginal text: \t{plain_text}")
    print(f"Cipher text: \t{cipher_text}")