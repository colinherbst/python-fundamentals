# 5-1

phone = 'iphone'
print("Is phone == 'iphone'? I predict True.")
print(phone == 'iphone')
print("Is phone == 'android'? I predict False.")
print(phone == 'android')

car = 'ferrari'
print("\nIs car == 'ferrari'? I predict True.")
print(car == 'ferrari')
print("Is car == 'tesla'? I predict False.")
print(car == 'tesla')

shoes = 'nike'
print("\nIs shoes == 'nike'? I predict True.")
print(shoes == 'nike')
print("Is shoes == 'adidas'? I predict False.")
print(shoes == 'adidas')

store = 'walmart'
print("\nIs store == 'walmart'? I predict True.")
print(store == 'walmart')
print("Is store == 'dillons'? I predict False.")
print(store == 'dillons')

restaurant = 'mcdonalds'
print("\nIs restaurant == 'mcdonalds'? I predict True.")
print(restaurant == 'mcdonalds')
print("Is restaraunt == 'popeyes'? I predict False.")
print(restaurant == 'popeyes')

# 5-2

# Tests for equality and inequality with strings

phone = 'iphone'
print("\nIs phone != 'iphone'? I predict False.")
print(phone != 'iphone')
print("Is phone != 'android'? I predict True.")
print(phone != 'android')


# Tests using the lower() method

print("\nIs phone == 'IPHONE'.lower()? I predict True.")
print(phone == 'IPHONE'.lower())

print("Is phone != 'iPhone'.lower()? I predict False.")
print(phone != 'iPhone'.lower())

# Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to

number = 2

print("\nIs number == 2? I predict True.")
print(number == 2)
print("Is number != 2? I predict False.")
print(number != 2)
print("Is number > 1? I predict True.")
print(number > 1)
print("Is number < 2? I predict False.")
print(number < 2)
print("Is number <= 2? I predict True.")
print(number <= 2)
print("Is number >= 3? I predict False.")
print(number >= 3)

# Test whether an item is in a list

list_check = [1, 2, 3, 4]
print("\nIs 1 in the list? I predict True.")
print(1 in list_check)

# Test whether an item is not in a list
print("Is 5 in the list? I predict False.")
print(5 in list_check)

# Write a function that will take 2 arguments.
# Inside the function provide examples of all the arithmetic operators.
# Provide a variable for each solution and print the results of each.


def arithmetic():

    num1 = 1 + 1
    num2 = 2 - 1
    num3 = 2 * 2
    num4 = 4 / 2
    num5 = 50 % 100
    num6 = 5 ** 2
    num7 = 5 // 2

    print(num1)
    print(num2)
    print(num3)
    print(num4)
    print(num5)
    print(num6)
    print(num7)


arithmetic()


# Write a function that takes only 1 argument.  Provide a variable for each solution and print the results of each.
# Inside the function provide examples of Assignment operators:
# modulus equals, minus equals, exponent equals & plus equals.
# Provide a variable for each solution and print the results of each.

def assignment():
    x = 10
    x %= 2
    print(x)
    x -= 4
    print(x)
    x **= 4
    print(x)
    x += 4
    print(x)


assignment()
