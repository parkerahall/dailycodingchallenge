def parse_words(string, dictionary):
    
    def parse_words_recur(string, dictionary, i):
        if len(string) == i:
            if string in dictionary:
                return True, [string]
            else:
                return False, []
        
        if string[:i] in dictionary:
            correct, words = parse_words_recur(string[i:], dictionary, 1)
            if correct:
                return True, [string[:i]] + words
        
        return parse_words_recur(string, dictionary, i + 1)

    correct, words = parse_words_recur(string, dictionary, 1)
    if correct:
        return words
    else:
        return None

string = "thequickbrownfox"
dictionary = set(["the", "quick", "brown", "fox"])
assert parse_words(string, dictionary) == ["the", "quick", "brown", "fox"]

string = "bedbathandbeyond"
dictionary = set(["bed", "bedbath", "and", "beyond"])
assert parse_words(string, dictionary) == ["bedbath", "and", "beyond"]

string = "bedbathandbeyond"
dictionary = set(["bed", "bedbath", "and", "beyond", "bath"])
assert (parse_words(string, dictionary) == ["bedbath", "and", "beyond"] or
        parse_words(string, dictionary) == ["bed", "bath", "and", "beyond"])