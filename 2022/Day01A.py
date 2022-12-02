import sys

previous = None
increases = 0

elves = []
total = 0

for line in sys.stdin:
    line = line.replace('\n', '')

    if not line:
        elves.append(total)
        total = 0
        continue
    
    current = int(line)
    
    if current == -1:
        break
        
    total += current    
    
print(max(elves))
