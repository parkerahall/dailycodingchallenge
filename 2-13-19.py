from collections import defaultdict

def single_search(matrix, start, word, i_diff, j_diff):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    index = 1
    i, j = start
    curr_i, curr_j = i + i_diff, j + j_diff
    while curr_i < num_rows and curr_j < num_cols:
        if word[index] == matrix[curr_i][curr_j]:
            if index == len(word) - 1:
                return True
            curr_i += i_diff
            curr_j += j_diff
            index += 1
        else:
            break
    return False

def word_search(characters, word):
    assert len(characters) > 0
    assert len(characters[0]) > 0

    num_rows = len(characters)
    num_cols = len(characters[0])

    letter_lookup = defaultdict(list)
    for i in range(num_rows):
        for j in range(num_cols):
            letter = characters[i][j]
            letter_lookup[letter].append((i, j))

    if word[0] not in letter_lookup:
        return False

    for start in letter_lookup[word[0]]:
        if single_search(characters, start, word, 1, 0):
            return True
        if single_search(characters, start, word, 0, 1):
            return True
    return False

characters = [ ["F", "A", "C", "I"],
               ["O", "B", "Q", "P"],
               ["A", "N", "S", "S"],
               ["M", "A", "S", "S"]]
foam = "FOAM"
mass = "MASS"
art = "ART"
flame = "FLAME"
grape = "GRAPE"
assert word_search(characters, foam) == True
assert word_search(characters, mass) == True
assert word_search(characters, art) == False
assert word_search(characters, flame) == False
assert word_search(characters, grape) == False