import numpy


def create_3d_array(num):
    return numpy.array(num)


num = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]

num3 = create_3d_array(num)
print('standard array', num, '\nnumpy array\n', num3)
