# Not happy with the brute force nature of this, but
# inspiration wasn't striking today

import sys

def calc_fuel(numbers, position):
    sum = 0
    
    for number in numbers:
        sum += abs(position-number)
        
    return sum

numbers = input()
numbers = [int(r) for r in numbers.split(',')]
numbers.sort()
min = numbers[0]
max = numbers[-1]

fuel = None

for current in range(min,max+1):
    temp = calc_fuel(numbers, current)
    
    if fuel is None or temp < fuel:
        fuel = temp

print(fuel)
