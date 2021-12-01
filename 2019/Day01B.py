import sys

numbers = []
total = 0

for line in sys.stdin:
    current = int(line)
    
    if current == -1:
        break
    
    fuel = current//3-2
    
    while fuel > 0:
        total += fuel
        fuel = fuel//3-2
    
print(total)
