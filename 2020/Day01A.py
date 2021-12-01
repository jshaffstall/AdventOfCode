import sys

numbers = []

for line in sys.stdin:
    current = int(line)
    
    if current == -1:
        break
    
    numbers.append(current)

for first in numbers:
    for second in numbers:
        if first+second == 2020:
            print(first*second)
            sys.exit()
            
