def make_function(i):
    def f():
        print(i)
    return f

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        flist.append(make_function(i))

    return flist

functions = make_functions()
for f in functions:
    f()