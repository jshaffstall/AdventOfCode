import sys

total = 0

for line in sys.stdin:
    current = int(line)
    
    if current == 0:
        break
    
    total += current
    
print(total)
