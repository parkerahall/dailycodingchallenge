def reg_ex_check(string, reg_ex):
    cached = {}
    for i in range(len(reg_ex)):
        cached[(len(string), i)] = False
    for i in range(len(string)):
        cached[(i, len(reg_ex))] = False
    cached[(len(string), len(reg_ex))] = True

    def reg_ex_dp(string_ind, reg_ex_ind, last):
        if (string_ind, reg_ex_ind) not in cached:
            if reg_ex[reg_ex_ind] == ".":
                cached[(string_ind, reg_ex_ind)] = reg_ex_dp(string_ind + 1, reg_ex_ind + 1, ".")
            elif reg_ex[reg_ex_ind] == "*":
                if last == "." or last == string[string_ind]:
                    cached[(string_ind, reg_ex_ind)] = reg_ex_dp(string_ind + 1, reg_ex_ind, last) or reg_ex_dp(string_ind, reg_ex_ind + 1, "*")
                else:
                    cached[(string_ind, reg_ex_ind)] = reg_ex_dp(string_ind, reg_ex_ind + 1, "*")
            elif string[string_ind] == reg_ex[reg_ex_ind]:
                cached[(string_ind, reg_ex_ind)] = reg_ex_dp(string_ind + 1, reg_ex_ind + 1, reg_ex[reg_ex_ind])
            else:
                if reg_ex_ind < len(reg_ex) - 1 and reg_ex[reg_ex_ind + 1] == "*":
                    cached[(string_ind, reg_ex_ind)] = reg_ex_dp(string_ind, reg_ex_ind + 2, "*")
                else:
                    cached[(string_ind, reg_ex_ind)] = False

        return cached[(string_ind, reg_ex_ind)]

    return reg_ex_dp(0, 0, "")

string = "ray"
reg_ex = "ra."
assert reg_ex_check(string, reg_ex) == True

string = "raymond"
reg_ex = "ra."
assert reg_ex_check(string, reg_ex) == False

string = "chat"
reg_ex = ".*at"
assert reg_ex_check(string, reg_ex) == True

string = "chats"
reg_ex = ".*at"
assert reg_ex_check(string, reg_ex) == False