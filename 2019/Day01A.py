import sys

numbers = []
total = 0

for line in sys.stdin:
    current = int(line)
    
    if current == -1:
        break
    
    total += int(current/3)-2

print(total)
