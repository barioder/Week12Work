# 1. Create a bubblesort algorithm that sort out 10 numbers in order.



# 2.Create a list called "bussinessdays" that prints out only 2 days in all
# uppercase.

bussinessdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

print(f'{bussinessdays[0].upper()} {bussinessdays[-1].upper()}')


print('---------------------------------------------------------')
# 3.Create a if statement that finds out if "sunday" is in your list. It will print
# an output of false.
if 'sunday' in bussinessdays:
    print(True)
else:
    print(False)

print('---------------------------------------------------------')
# 4.Create a class function that has a child class inherit from a parent class.

class Animal:
    def __init__(self, name, year):
        self.name = name
        self.year = year


class Cat(Animal):
    def describe(self):
        print(f'This is {self.name} a {self.year} year old Cat')

class Dog(Animal):
    def describe(self):
        print(f'This is {self.name} a {self.year} year old Dog')


a = Cat('Kitty', 2)
a.describe()

b = Dog('Max', 4)
b.describe()


list = [5, 6, 12, 7, 9, 10]
print(len(list))

for i in range(0,len(list)-1):
    print(i)

for i in range(0, 5):
    print(i)


def bubble_sort(list1):
    # Outer loop for traverse the entire list
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if (list1[j] > list1[j + 1]):
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1


list1 = [5, 3, 8, 6, 7, 2, 1]

print(bubble_sort(list1))