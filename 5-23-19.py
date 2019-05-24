def shortest_unique_prefixes(words):
    prefixes = [[] for _ in words]
    to_do = set([i for i in range(len(words))])
    string_index = 0
    while len(to_do) > 0:
        letters = {}
        new_to_do = set()
        
        for word_index in to_do.copy():
            if string_index >= len(words[word_index]):
                prefixes[word_index] = []
                to_do.remove(word_index)

        for word_index in to_do:
            word = words[word_index]
            letter = word[string_index]
            if letter not in letters:
                letters[letter] = []
            letters[letter].append(word_index)

        for letter in letters:
            keep_going = len(letters[letter]) > 1
            for word_index in letters[letter]:
                prefixes[word_index].append(letter)

                if keep_going:
                    new_to_do.add(word_index)

        to_do = new_to_do
        string_index += 1

    return ["".join(prefix) for prefix in prefixes]

words = ["dog", "cat", "apple", "apricot", "fish"]
expected = ["d", "c", "app", "apr", "f"]
assert shortest_unique_prefixes(words) == expected

words = ["apple", "apricot", "app"]
expected = ["appl", "apr", ""]
assert shortest_unique_prefixes(words) == expected