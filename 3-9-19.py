DIRECTIONS = ["N", "S", "E", "W"]

DIRECTION_SWAP = {"N": "S", "S": "N", "E": "W", "W": "E"}

def is_invalid(cmp_dict, first, second, rule):
    for direction in DIRECTIONS:
        if direction in rule:
            oppo_direction = DIRECTION_SWAP[direction]
            if first in cmp_dict[second][direction] or second in cmp_dict[first][oppo_direction]:
                return True
    return False

def apply_rule(cmp_dict, first, second, rule):
    for direction in DIRECTIONS:
        if direction in rule:
            oppo_direction = DIRECTION_SWAP[direction]
            
            cmp_dict[first][direction].add(second)
            cmp_dict[first][direction] |= cmp_dict[second][direction]

            cmp_dict[second][oppo_direction].add(first)
            cmp_dict[second][oppo_direction] |= cmp_dict[first][oppo_direction]

def check_valid(rules):
    cmp_dict = {}
    for rule in rules:
        first, compare, second = rule.split(" ")
        if first not in cmp_dict:
            cmp_dict[first] = {direction : set() for direction in DIRECTIONS}
        if second not in cmp_dict:
            cmp_dict[second] = {direction : set() for direction in DIRECTIONS}

        if is_invalid(cmp_dict, first, second, rule):
            return False

        apply_rule(cmp_dict, first, second, rule)
    return True

rules = ["A N B", "B NE C", "C N A"]
assert check_valid(rules) == False

rules = ["A NW B", "A N B"]
assert check_valid(rules) == True