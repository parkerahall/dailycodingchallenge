class Doubleton:
    class __Inner:
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return str(self.value)
    
    first = None
    second = None
    init_count = 0
    get_count = 0
    
    def __init__(self, arg):
        if Doubleton.first == None:
            Doubleton.first = Doubleton.__Inner(arg)
        elif Doubleton.second == None:
            Doubleton.second = Doubleton.__Inner(arg)
        elif init_count % 2:
            Doubleton.first.value = arg
        else:
            Doubleton.second.value = arg
        Doubleton.init_count += 1

    def __getattr__(self, attr):
        Doubleton.get_count += 1
        if Doubleton.get_count % 2:
            return getattr(self.first, attr)
        else:
            return getattr(self.second, attr)

first = Doubleton('hello')
second = Doubleton('goodbye')

for _ in range(10):
    print(first.value)

for _ in range(10):
    print(second.value)