import sys

changes = []
total = 0

for line in sys.stdin:
    current = int(line)
    
    if current == 0:
        break
    
    changes.append(current)
    
frequencies = {}
current = 0

while True:
    total += changes[current]
    current = (current+1)%len(changes)
    
    if total in frequencies:
        print(total)
        sys.exit()
        
    frequencies[total] = 1
    
