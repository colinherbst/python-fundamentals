# 2-8 Number Eight

print(4+4)
print(10-2)
print(4*2)
print(16/2)

# 2-9 Favorite Number

favorite_number = 10
print(f'My favorite number is: {favorite_number}')

# Assign variables to following sets of numbers.
# Use underscores to make them more readable.
# Write a function called number_sets and print each variable inside the function.
# Call all the function to verify your results.

# 456234 68423791 13794628 96374

number1 = 456_234
number2 = 68_423_791
number3 = 13_794_628
number4 = 96_374


def number_sets():
    print(number1, number2, number3, number4)


number_sets()

# Write a function that will take 2 arguments.
# Using Type conversion, convert the first argument from int to float.
# Convert the second argument from float to int.
# Call the function and provide the correct values for each argument to verify your results.
# One argument should be a float and the other an int.


def float_int():
    print(float(number1), int(number2))


float_int()

# Write a function that will have two inputs.
# The first input method should ask “What is your favorite movie”.
# The second input method should ask “How many times have you seen it?”.
# The second input should be inside an int function.
# Each input method should be assigned to a variable.
# In a print statement using placeholders,
# the output result should be “I have seen {favorite movie} {number of times} times”.


def favorite_movie():
    fav_movie = input('What is your favorite movie? ')
    fav_movie_seen = input('How many times have you seen it? ')
    print(f'I have seen {fav_movie} {fav_movie_seen} times')


favorite_movie()
