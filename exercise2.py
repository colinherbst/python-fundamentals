# Write a function called simple(). Assign a different message to 5 variables and print each message.

def simple():
    """Animals"""
    animal1 = 'Cow'
    animal2 = 'Pig'
    animal3 = 'Horse'
    animal4 = 'Sheep'
    animal5 = 'Chicken'

    print(animal1)
    print(animal2)
    print(animal3)
    print(animal4)
    print(animal5)


simple()


# Write a function called simple2().
# Assign a message to a variable, then print out that variable.
# Change the message and assign it to the variable again, but after the first print statement.
# Print the second message. Do these steps 2 more times.
# You should have 4 messages assigned to the same variable and 4 print functions showing the results.

def simple2():
    animal = 'Cow'
    print(animal)
    animal = 'Pig'
    print(animal)
    animal = 'Horse'
    print(animal)
    animal = 'Sheep'
    print(animal)


simple()


# Write a function called message that takes 1 argument.
# Inside that function, write a print function that takes the argument.

def message(strawberry):
    print(strawberry + ' Flavor')


message('Strawberry')
