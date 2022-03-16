# 10-6 and 10-7
print("Type 'break' to quit.\n")
while True:
    try:
        x = input("Enter a number: ")
        if x == 'break':
            break
        x = int(x)
        y = input("Enter another number: ")
        if y == 'break':
            break
        y = int(y)
    except ValueError:
        print("You need to enter a number")
    else:
        plus = x + y
        print(str(x) + " plus " + str(y) + " is " + str(plus) + ".")


# 10-8 and 10-9
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print("\nfile: " + filename)
        print(contents)
