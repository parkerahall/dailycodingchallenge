def palindromable_brute(string, k, j=0):
    if type(string) == str:
        string = list(string)

    if string == string[::-1]:
        return True
    elif k == 0:
        return False

    good = False
    for i in range(j, len(string)):
        new_string = string[:i] + string[i + 1:]
        good = good or palindromable_brute(new_string, k - 1, i)
    return good

def palindromable(string, k):
    
    memo = {}
    target = string[::-1]
    
    def edit_distance(i, j, k):
        if (i, j, k) not in memo:
            if i == len(string) or j == len(target):
                memo[(i, j, k)] = k >= abs(i - j)
            elif string[i] == target[j]:
                memo[(i, j, k)] = edit_distance(i + 1, j + 1, k)
            elif k > 0:
                value = edit_distance(i + 1, j, k - 1) or edit_distance(i, j + 1, k - 1)
                memo[(i, j, k)] = value
            else:
                memo[(i, j, k)] = False
        return memo[(i, j, k)]
    
    return edit_distance(0, 0, 2 * k)


string = "waterrfetawx"
k = 2
assert palindromable_brute(string, k) == True

string = "waterrfetawx"
k = 1
assert palindromable_brute(string, k) == False

string = "waterrfetawx"
k = 2
assert palindromable(string, k) == True

string = "waterrfetawx"
k = 1
assert palindromable(string, k) == False