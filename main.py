import numpy as np


# create an array
def create_array(size):
    return np.arange(size)


def array_info(arr):
    print('array:\n', arr)
    print('shape:',
          arr.shape)  # array shape, This is a tuple of integers indicating the size of the array in each dimension
    print("dimensions:", arr.ndim)  # the number of axes (dimensions) of the array.
    print("size:",
          arr.size, '\n')  # the total number of elements of the array. This is equal to the product of the elements of shape.


my_arr = create_array(15)
array_info(my_arr)

my_arr = my_arr.reshape(3, 5)

array_info(my_arr)
