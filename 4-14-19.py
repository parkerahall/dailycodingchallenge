DIGITS = set([str(i) for i in range(10)])
NEG = '-'
DOT = '.'
E = 'e'

def is_pos_int(string):
    return all([char in DIGITS for char in string])

def is_neg_int(string):
    return string[0] == NEG and all([char in DIGITS for char in string[1:]]) and len(string) > 1

def is_real_num(string):
    first_dot = len(string)
    for i in range(len(string)):
        if string[i] == DOT:
            first_dot = i
            break

    return (is_pos_int(string[:first_dot]) or is_neg_int(string[:first_dot])) and (is_pos_int(string[first_dot + 1:]))

def is_scientific_num(string):
    first_e = len(string)
    for i in range(len(string)):
        if string[i] == E:
            first_e = i
            break

    return is_real_num(string[:first_e]) and (is_pos_int(string[first_e + 1:]) or is_neg_int(string[first_e + 1:]))

def is_number(string):
    number_funcs = [is_pos_int, is_neg_int, is_real_num, is_scientific_num]
    return any([func(string) for func in number_funcs])

good_nums = ["10", "-10", "10.1", "-10.1", "1e5"]
assert all([is_number(string) for string in good_nums])

bad_nums = ["a", "x 1", "a -2", "a-2", "-"]
assert not any([is_number(string) for string in bad_nums])