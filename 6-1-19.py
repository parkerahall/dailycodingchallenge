def is_enter(entry):
    return entry["type"] == "enter"

def busiest_period(entries):
    entries.sort(key=lambda x: x["timestamp"])

    max_people = 0
    people = 0
    best_enter = None
    best_exit = None
    for entry in entries:
        people_entered = is_enter(entry)
        
        if people == max_people and not people_entered:
            best_exit = entry["timestamp"]
        
        modifier = 1 if people_entered else -1
        people += entry["count"] * modifier
        max_people = max(max_people, people)

        if people == max_people:
            best_enter = entry["timestamp"]

    return best_enter, best_exit

def make_entry(time, count, typ):
    return {"timestamp": time, "count": count, "type": typ}

entries = [make_entry(1, 3, "enter"), make_entry(4, 2, "exit"), make_entry(2, 2, "exit"), make_entry(3, 1, "enter")]
assert busiest_period(entries) == (1, 2)