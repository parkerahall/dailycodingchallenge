def div(x, y):
    if y == 0:
        return x
    return x / y

def partial_product(l):
    product = 1
    num_zeros = 0
    last_zero_ind = -1
    for i in range(len(l)):
        if l[i] == 0:
            num_zeros += 1
            last_zero_ind = i
        else:
            product *= l[i]

    output = [0] * len(l)
    if num_zeros > 0:
        if num_zeros == 1:
            output[last_zero_ind] = product
    else:
        for i in range(len(l)):
            output[i] = div(product, l[i])
    return output

l = [3, 2, 0, 0, 0]
print(partial_product(l))