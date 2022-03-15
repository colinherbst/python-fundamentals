# 5-3 Alien Colors #1
alien_color = 'green'

if alien_color == 'green':
    print('You have earned 5 points!')

if alien_color == 'yellow':
    print('You have earned 5 points!')

# 5-4 Alien Colors #2
if alien_color == 'green':
    print('You have earned 5 points for shooting the alien!')
else:
    print('You have earned 10 points')

# 5-5 Alien Colors #3

alien_color = 'red'

if alien_color == 'green':
    print("You have earned 5 points!")
elif alien_color == 'yellow':
    print("You have earned 10 points!")
else:
    print("You have earned 15 points!")

alien_color = 'yellow'

if alien_color == 'green':
    print("You have earned 5 points!")
elif alien_color == 'yellow':
    print("You have earned 10 points!")
else:
    print("You have earned 15 points!")

alien_color = 'green'

if alien_color == 'green':
    print("You have earned 5 points!")
elif alien_color == 'yellow':
    print("You have earned 10 points!")
else:
    print("You have earned 15 points!")

# 5-6 Stages of Life

print('Enter your age')
age = int(input())

if age < 2:
    print("You're a baby")
elif age < 4:
    print("You're a toddler")
elif age < 13:
    print("You're a kid")
elif age < 20:
    print("You're a teenager")
elif age < 65:
    print("You're an adult")
else:
    print("You're an elder")

# 5 Write a function that takes an argument.
# Check this argument to see if it is a Boolean using the bool method.
# Call the method and use the below values as your argument.
# Using comments, provide the name of the argument and if it was true or false from running the code.


def boolean():
    check = 12
    print(bool(check))
    check = 1.2
    print(bool(check))
    check = 0
    print(bool(check))
    check = 0.4
    print(bool(check))
    check = 0.0
    print(bool(check))


boolean()

# 12 = True
# 1.2 = True
# 0 = False
# 0.4 = True
# 0.0 = False
