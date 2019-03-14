# below code will print 9 10 times, as 9 is the last value of i

"""
functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
"""

def lambda_maker(i):
    return lambda : i

functions = []
for i in range(10):
    functions.append(lambda_maker(i))

for f in functions:
    print(f())