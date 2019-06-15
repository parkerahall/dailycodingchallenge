def GCD(numbers):
    smallest = min(numbers)
    for factor in range(smallest, 1, -1):
        if not any([x % factor for x in numbers]):
            return factor

numbers = [42, 56, 14]
assert GCD(numbers) == 14

numbers = [48, 108, 84, 12000]
assert GCD(numbers) == 12