__author__ = 'ypw'

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print squares   # Prints [0, 1, 4, 9, 16]

squares = [x ** 2 for x in nums]
print squares   # Prints [0, 1, 4, 9, 16]

even_squares = [x ** 2 for x in nums if x % 2 == 0]
print even_squares
