import sys

line = input()
numbers = [int(r) for r in line.split(',')]
day = 0

while day < 80:
    num_zeroes = numbers.count(0)
    numbers = [6 if r == 0 else r-1 for r in numbers]
    numbers += [8]*num_zeroes
    day += 1
    
print(len(numbers))

