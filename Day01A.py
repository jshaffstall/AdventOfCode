import sys

previous = None
increases = 0

for line in sys.stdin:
    current = int(line)
    
    if current == -1:
        break
    
    if previous and current > previous:
        increases += 1
        
    previous = current
    
print(increases)
