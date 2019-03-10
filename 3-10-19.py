import numpy as np

def divide(a, b):
    num = 0
    while a >= b:
        num += 1
        a -= b
    return num

N = 1000
for _ in range(N):
    a = np.random.randint(N)
    b = np.random.randint(N)
    while b == 0:
        b = np.random.randint(N)

    assert divide(a, b) == a / b