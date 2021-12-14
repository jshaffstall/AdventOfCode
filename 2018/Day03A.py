import sys

def check_overlap(claim1, claim2):
    dx = min(claim1['x2'], claim2['x2']) - max(claim1['x1'], claim2['x1'])
    dy = min(claim1['y2'], claim2['y2']) - max(claim1['y1'], claim2['y1'])
    if (dx>=0) and (dy>=0):
        return dx*dy
    
    return 0

claims = []

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break
    
    id,rest = line.split('@')
    position,size = rest.split(':')
    x,y = [int(r) for r in position.split(',')]
    width,height = [int(r) for r in size.split('x')]
    
    claims.append({
        'id': id.strip(),
        'x' : x,
        'y' : y,
        'width' : width,
        'height' : height
    })
    
grid = {}

for claim in claims:
    for x in range(claim['x'], claim['x']+claim['width']):
        for y in range(claim['y'], claim['y']+claim['height']):
            if (x,y) not in grid:
                grid[(x,y)] = 0
                
            grid[(x,y)] += 1
        
    
print(len([1 for r in grid if grid[r] > 1]))
