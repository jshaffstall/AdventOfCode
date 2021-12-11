# I spent an embarrassingly long time not reading the instructions closely enough,
# and not changing the 1 and 2 elements.

import sys

line = input()
numbers = [int(r) for r in line.split(',')]
numbers[1] = 12
numbers[2] = 2
index = 0

while True:
    if numbers[index] == 1:
        numbers[numbers[index+3]] = numbers[numbers[index+1]]+numbers[numbers[index+2]]
    elif numbers[index] == 2:
        numbers[numbers[index+3]] = numbers[numbers[index+1]]*numbers[numbers[index+2]]
    elif numbers[index] == 99:
        break
    
    index += 4

print(numbers[0])
