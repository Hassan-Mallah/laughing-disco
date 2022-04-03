import numpy as np


# create an array
def create_array(size):
    return np.arange(size)


arr = create_array(15)
a = arr.reshape(3, 5)

print('array:\n', a)
print('shape:', a.shape)
