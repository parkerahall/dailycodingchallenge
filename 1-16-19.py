def segregate(array):
    num_r = 0
    num_g = 0
    num_b = 0
    index = 0
    while index < len(array) - num_b:
        move = True
        if array[index] == "R":
            if index > num_r:
                array[index], array[num_r] = array[num_r], array[index]
                move = False
            num_r += 1
        elif array[index] == "G":
            if index > num_r + num_g:
                array[index], array[num_r + num_g] = array[num_r + num_g], array[index]
                move = False
            if index == num_r + num_g:
                num_g += 1
        elif array[index] == "B":
            if index < len(array) - num_b - 1:
                array[index], array[len(array) - num_b - 1] = array[len(array) - num_b - 1], array[index]
                move = False
            num_b += 1
        else:
            raise ValueError

        if move:
            index += 1

array = ["G", "B", "R", "R", "B", "R", "G"]
segregate(array)
assert array == ["R", "R", "R", "G", "G", "B", "B"]