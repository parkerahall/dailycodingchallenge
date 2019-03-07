import numpy as np

def x_or_y(x, y, b):
    low_mask = 2 ** 32 - 1
    x_mask = (2 ** 32 - b) & low_mask
    y_mask = (2 ** 32 - (1 - b)) & low_mask
    return (x & x_mask) | (y & y_mask)

max_value = 2 ** 32
for _ in range(100):
    x = np.random.randint(0, max_value)
    y = np.random.randint(0, max_value)

    assert x_or_y(x, y, 1) == x
    assert x_or_y(x, y, 0) == y