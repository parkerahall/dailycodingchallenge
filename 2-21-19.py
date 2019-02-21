import random

def rand7():
    return random.randint(1, 7)

def rand5():
    number = rand7()
    while number > 5:
        number = rand7()
    return number

N = 10000
dic = {(i + 1) : 0. for i in range(5)}
for _ in range(N):
    dic[rand5()] += 1.
for key in dic:
    dic[key] -= (N / 5.)
    dic[key] /= (N / 5.)
print dic