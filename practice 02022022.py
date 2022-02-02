# # value = 'The Boys are like very crazy today for a verylongwhile'
# #
# # c = value.split(' ')
# #
# # print(c)
# #
# # def my_func(f, arg):
# #   return f(arg)
# #
# # print(my_func(lambda x: 2*x*x, 5))
# #
# # print((lambda x: x**2 + 5*x + 4)(-1) )
# print('-----------------------------')
# import numpy as np
# arr1 = np.array([1, 2, 3, 4, 5, 6])
# print(arr1)
# print(arr1.ndim)
#
#
# z = arr1[1]*arr1[3]
# print(z)
# print(arr1)
# #                   r c
# print(arr1.reshape(3, 2))
#
# print(arr1.reshape(2, 3))

list1 = [22, 10, 13, 71, 8, 12, 61, 68]

z = len(list1)
n = 0
while z > 0:
    # n = 1 + n
    for j in range(len(list1) - 1):
        if (list1[j] > list1[j + 1]):
            temp = list1[j]
            list1[j] = list1[j + 1]
            list1[j + 1] = temp
            print(list1)
    z = z - 1
    print(z)
print(list1)

import  numpy as np
# 3.Create a 6-D array and reshape it to another size.

arr2 = np.array([[[[[[11, 23, 22, 42, 25, 62], [27, 82, 59, 10, 11, 12], [13, 14, 15, 16, 17, 18],
                     [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]]]]])
print(arr2.ndim)
print(arr2.shape)
print(arr2.reshape(4, 9))

arr3 = arr2.reshape(12, 3)
print(arr3)
print(arr3.ndim, 'for 3')
