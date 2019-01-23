def find_pair(l, k):
    partners = set()
    for elt in l:
        if (k - elt) in partners:
            return True
        partners.add(elt)
    return False

l = [10, 15, 3, 7]
k = 17
print(find_pair(l, k))