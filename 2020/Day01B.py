import sys

numbers = []

for line in sys.stdin:
    current = int(line)
    
    if current == -1:
        break
    
    numbers.append(current)

for first in numbers:
    for second in numbers:
        for third in numbers:
            if first+second+third == 2020:
                print(first*second*third)
                sys.exit()

