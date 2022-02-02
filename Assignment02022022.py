# 1.Create a bubblesort algorithm using a while loop.
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

    z = z - 1
print(list1)
print('------------------------------------------------')
# 2.Create a numpy array using a function that prints out
# how many dimension is your array.
import numpy as np
myArray = np.array([10, 20, 30, 40, 50])
print('The Number of dimension is ', myArray.ndim)
print('------------------------------------------------')
# 3.Create a 6-D array and reshape it to another size.

arr2 = np.array([[[[[[11, 23, 22, 42, 25, 62], [27, 82, 59, 10, 11, 12], [13, 14, 15, 16, 17, 18],
                     [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]]]]])

print(arr2.reshape(4, 9))
print('------------------------------------------------')
# 4.Create a forloop that prints your name 5 times.

n = 5
Name = 'Derrick'
for i in range(n):
    print(i+1, '.', Name)

print('------------------------------------------------')
# 5.Create a list and convert it back into a tuple.
name_list = ['Stevo', 'Derrick', 'Tim']
tup = tuple(name_list)
print(tup)

