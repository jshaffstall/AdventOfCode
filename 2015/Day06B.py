import sys

lights = [[False for r in range(1000)] for r in range(1000)]

for line in sys.stdin:
    if line.strip() == '-1':
        break

    amount = 2
    rest = line[7:]
    
    if line.startswith('turn on'):
        amount = 1
        rest = line[8:]
        
    if line.startswith('turn off'):
        amount = -1
        rest = line[9:]
    
    start, end = rest.split('through')
    startx, starty = start.split(',')
    startx, starty = int(startx), int(starty)
    endx, endy = end.split(',')
    endx, endy = int(endx), int(endy)
    
    for row in range(starty, endy+1):
        for col in range(startx, endx+1):
            lights[row][col] = max(lights[row][col]+amount, 0)
            
print(sum([sum(r) for r in lights]))                
