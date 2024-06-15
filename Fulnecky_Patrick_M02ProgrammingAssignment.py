# Author: Patrick Fulnecky
# Programming Assignments for M02.
# These include 4.1, 4.2, 6.1, 6.2, and 6.3

# 4.1
secret = 7
guess = 5

if secret == guess:
    print ('just right')
elif secret > guess:
    print('too low')
else: print('too high')

#4.2
small = True
green = False

if small == True:
    if green == True:
        print('pea')
    else:
        print('cherry')
else:
    if green == True:
        print('watermelon')
    else:
        print('pumkin')

#6.1
myList = [3, 2, 1, 0]

for i in myList:
    print(i)

#6.2 v1
guess_me = 7
number = 1

while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it')
        break
    else:
        print('oops')
        break
    number += 1




