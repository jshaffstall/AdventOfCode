import sys

previous = None
position = 0
depth = 0

for line in sys.stdin:
    line = line.strip()
    
    if line == '-1':
        break
    
    if line.startswith('forward'):
        amount = int(line[7:])
        position += amount
        
    if line.startswith('down'):
        amount = int(line[4:])
        depth += amount
    
    if line.startswith('up'):
        amount = int(line[2:])
        depth -= amount
        
print(position*depth)
