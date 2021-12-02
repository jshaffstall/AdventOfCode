import sys

lights = [[False for r in range(1000)] for r in range(1000)]

for line in sys.stdin:
    if line.strip() == '-1':
        break

    action = None
    rest = line[7:]
    
    if line.startswith('turn on'):
        action = True
        rest = line[8:]
        
    if line.startswith('turn off'):
        action = False
        rest = line[9:]
    
    start, end = rest.split('through')
    startx, starty = start.split(',')
    startx, starty = int(startx), int(starty)
    endx, endy = end.split(',')
    endx, endy = int(endx), int(endy)
    
    for row in range(starty, endy+1):
        for col in range(startx, endx+1):
            if action is None:
                lights[row][col] = not lights[row][col]
            else:
                lights[row][col] = action
                
print(sum([r.count(True) for r in lights]))                
