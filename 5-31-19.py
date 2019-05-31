def is_one_off(first, second):
    diff = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            diff += 1
    return diff < 2

def find_path(end, parent):
    path = []
    current = end
    while current != None:
        path.append(current)
        current = parent[current]
    return path[::-1]

def word_ladder(words, start, end):
    words.append(start)
    adj = {word: [] for word in words}
    
    for i in range(len(words)):
        first = words[i]
        for j in range(i + 1, len(words)):
            second = words[j]
            if is_one_off(first, second):
                adj[first].append(second)
                adj[second].append(first)

    parent = {start : None}
    frontier = [start]
    found = False
    while len(frontier) > 0:
        new_frontier = []
        for word in frontier:
            for adj_word in adj[word]:
                if adj_word not in parent:
                    parent[adj_word] = word
                    new_frontier.append(adj_word)
                if adj_word == end:
                    return find_path(end, parent)
        frontier = new_frontier

    return None

start = "dog"
end = "cat"
words = ["dot", "dop", "dat", "cat"]
expected = ["dog", "dot", "dat", "cat"]
actual = word_ladder(words, start, end)
assert actual == expected

start = "dog"
end = "cat"
words = ["dot", "tod", "dat", "dar"]
expected = None
actual = word_ladder(words, start, end)
assert actual == expected

start = "dog"
end = "cat"
words = ["dot", "tod", "dar", "cat"]
expected = None
actual = word_ladder(words, start, end)
assert actual == expected