def min_value(dictionary):
    smallest = float('inf')
    for key in dictionary:
        if dictionary[key] == None:
            return False, False
        smallest = min(smallest, dictionary[key])
    return True, smallest

def shortest_substring_with_letters(string, letters):
    letter_to_index = {letter : None for letter in letters}
    shortest_string = None
    shortest_length = len(string)

    for i in range(len(string)):
        current_letter = string[i]
        if current_letter in letters:
            letter_to_index[current_letter] = i
            all_found, start = min_value(letter_to_index)
            if all_found:
                if i - start + 1 < shortest_length:
                    shortest_length = i - start + 1
                    shortest_string = string[start:i + 1]

    return shortest_string

string = "figehaeci"
letters = set(["a", "e", "i"])
assert shortest_substring_with_letters(string, letters) == "aeci"