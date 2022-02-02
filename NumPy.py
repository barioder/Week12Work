import numpy as np


arr1 = np.array([1,2,3,4,5,6]) #1-D array
arr2 = np.array([1,2,3,4,5,6],ndmin = 5) #ndmin for the numbers of added brackets
arr3 = np.array([[1,2,3,4],[5,6,7,8]])
arr4 = np.array([[[10,20,30,40],[50,60,70,80],[90,100,110,120]]])
arr5 = np.array([[[[5,10,15,20],[25,30,35,40],[45,50,55,60],[65,70,75,80]]]])
"""
[[1,2,3,5]
  5,6,7,8]]


"""



print(arr1)
print(arr1.ndim) #Number of dimension
print(arr2)
print(arr2.ndim)
print(arr3)
print(arr3.ndim)
print(arr4)
print(arr4.ndim)
print(arr5)
print(arr5.ndim)

#                  r c
print(arr3.reshape(2,4)) #Reshape your current array
print(arr4.reshape(2,6))
print(arr1.reshape(3,2))


def array_values(n):
    y = np.array(arr1)
    return n + str(y)
print(array_values("The array: "))

list1 = [22, 10, 13, 71, 8, 12, 61, 68]

print(len(list1))

for i in range(7):
    print(i)