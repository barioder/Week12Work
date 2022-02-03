# Today's Assignment, due 6.40 pm EAT/ 10.40am US Eastern Time today. As usual email solutions to shawnday.dl@gmail.com
#
# 1.Create "two" 2-D array and divide each array of both 2-D array.
import numpy as np
num1 = np.array([[1, 2, 3, 4], [4, 6, 7, 8]])
num2 = np.array([[9, 10, 11, 12], [13, 14, 15, 16]])

print(num1/num2)

print('--------------------------------------------------------------')

# 2.Create a game using if statements and user inputs.
import random
userInput = input("Guess a number between 1-10 ")
x = random.randint(1, 10)
if userInput == x:

    print('!!WIN!!')
else:
    print('Wrong, mine was ', x)
    print('Sorry Try Again')
print('--------------------------------------------------------------')
# 3.Create a list and pop and replace an element out of your list,
# then convert it to a tuple.

list = [1, 2, 3, 5]
a = list.pop()

print(a)

list.append(4)
print(list)

print('Our Tuple ', tuple(list))

print('--------------------------------------------------------------')
# 4.Create a "L" pattern object using the letter "L"
n = 5
while True:
    if n > 1:
        print('L')

    if n == 1:
        print('L'*5)

    if n == 0:
        break

    n -= 1

print('--------------------------------------------------------------')
# 5.Create a while loop that prints your name 10 times.
n = 10
y = 0
while True:
    y += 1
    if n > 0:

        print(y, 'Derrick')
        n -= 1
    else:
        break
