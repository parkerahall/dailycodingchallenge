from collections import deque
from collections import defaultdict

def itinerary(flights, source):
    num_flights = len(flights)
    
    neighbors = defaultdict(list)
    for origin, destination in flights:
        neighbors[origin].append(destination)

    paths = deque([[(None, source)]])
    possible = []
    while len(paths) > 0:
        current_path = paths.popleft()
        current_flight = current_path[-1]
        current_city = current_flight[1]

        for next_city in neighbors[current_city]:
            if (current_city, next_city) not in current_path:
                new_path = current_path + [(current_city, next_city)]
                if len(new_path) == num_flights + 1:
                    possible.append(new_path)
                else:
                    paths.append(new_path)

    if len(possible) == 0:
        return None

    for i in range(len(possible)):
        edges = possible[i]
        nodes = []
        for source, dest in edges:
            nodes.append(dest)
        possible[i] = nodes

    possible.sort()
    return possible[0]

flights = [("SFO", "HKO"), ("YYZ", "SFO"), ("YUL", "YYZ"), ("HKO", "ORD")]
source = "YUL"
assert itinerary(flights, source) == ["YUL", "YYZ", "SFO", "HKO", "ORD"]

flights = [("SFO", "COM"), ("COM", "YYZ")]
source = "COM"
assert itinerary(flights, source) == None

flights = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "A")]
source = "A"
assert itinerary(flights, source) == ["A", "B", "C", "A", "C"]