import sys

def calc_fuel(numbers, position):
    cost = 0
    
    for number in numbers:
        cost += sum(range(abs(position-number)+1))
        
    return cost

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
