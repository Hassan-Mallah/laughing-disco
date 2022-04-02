import numpy


def create_3d_array(num):
    num3 = numpy.array(num)
    print('standard array', num, '\nnumpy array\n', num3)

    print('num3.dtype: ', num3.dtype)


arr2 = [[[1, 2, 3], [4, 5, 6]]]
arr3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

num2 = numpy.array(arr2)
print(num2)
print('num2.dtype: ', num2.dtype)
create_3d_array(arr3)
