def is_shifted(A, B):
    start = 0
    A_len = len(A)
    while start < A_len:
        correct = True
        for i in range(A_len):
            correct = correct and A[(start + i) % A_len] == B[i]
        if correct:
            return True
        start += 1
    return False

A = "abcde"
B = "cdeab"
assert is_shifted(A, B) == True

A = "abc"
B = "acb"
assert is_shifted(A, B) == False