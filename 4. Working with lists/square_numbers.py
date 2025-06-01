# squares = []
# for value in range(1, 11):
#    squares.append(value**2)

#print(squares)


numbers = list(range(0, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))


odd_numbers = list(range(3, 31, 3))
for number in odd_numbers:
    print(number)

cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
    print(cube)
