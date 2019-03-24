def permutations(digits):
    perms = [([], set())]
    for _ in range(len(digits)):
        new_perms = []
        for perm, used in perms:
            for i in range(len(digits)):
                if i not in used:
                    new_used = used.copy()
                    new_used.add(i)
                    new_perms.append((perm + [digits[i]], new_used))
        perms = new_perms
    return [x[0] for x in perms]

digits = [1, 2, 3]
expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
actual = permutations(digits)
assert len(expected) == len(actual)
for elt in expected:
    assert elt in actual