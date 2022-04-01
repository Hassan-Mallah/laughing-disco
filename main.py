import numpy


def create_3d_array(num):
    num3 = numpy.array(num)
    print('standard array', num, '\nnumpy array\n', num3)


num = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]

create_3d_array(num)
