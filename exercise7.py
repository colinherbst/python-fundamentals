# 4-3 Counting to Twenty
numbers = list(range(1, 21))
for number in numbers:
    print(number)

# 4-6 Odd Numbers
for number in range(1, 20, 2):
    print(number)

# 4-7 Threes
threes = list(range(3, 31, 3))
for number in threes:
    print(number)

# 4-8 Cubes
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
for cube in cubes:
    print(cube)
