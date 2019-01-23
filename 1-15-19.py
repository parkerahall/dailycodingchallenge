def palindrome_finder_fewest(string):
    letters = []
    additions = 0
    front = 0
    back = len(string) - 1
    while front <= back:
        if string[front] == string[back]:
            letters.append(string[front])
            front += 1
            back -= 1
        else:
            letters.append(string[back])
            additions += 1
            back -= 1
    if (len(string) + additions) % 2:
        return "".join(letters) + "".join(letters[:-1][::-1])
    else:
        return "".join(letters) + "".join(letters[::-1])

string = "race"
assert palindrome_finder_fewest(string) == "ecarace"

string = "google"
assert palindrome_finder_fewest(string) == "elgoogle"

def palindrome_finder_first(string):
    front_half = []
    back_half = []
    front = 0
    back = len(string) - 1
    while front <= back:
        if front == back:
            front_half.append(string[front])
            break

        front_half.append(min(string[front], string[back]))
        back_half.append(min(string[front], string[back]))
        
        back_diff = 0
        front_diff = 0
        if string[front] >= string[back]:
            back_diff = 1
        if string[front] <= string[back]:
            front_diff = 1
        front += front_diff
        back -= back_diff
    
    return "".join(front_half) + "".join(back_half[::-1])

string = "race"
assert palindrome_finder_first(string) == "ecarace"

string = "google"
assert palindrome_finder_first(string) == "eglgooglge"