def palindromable(word):
    chars = set()
    for char in word:
        if char in chars:
            chars.remove(char)
        else:
            chars.add(char)
    return len(chars) == 1

word = "carrace"
assert palindromable(word) == True

word = "daily"
assert palindromable(word) == False