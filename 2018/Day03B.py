import sys

def overlaps(claim1, claim2):
    dx = min(claim1['x2'], claim2['x2']) - max(claim1['x1'], claim2['x1'])
    dy = min(claim1['y2'], claim2['y2']) - max(claim1['y1'], claim2['y1'])
    if (dx>=0) and (dy>=0):
        return dx*dy
    
    return 0

claims = []
ids = []

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
        'x1' : x,
        'y1' : y,
        'x2' : x+width,
        'y2' : y+height
    })
    
    ids.append(id.strip())
    
for index,claim in enumerate(claims):
    for index2 in range(index+1, len(claims)):
        if overlaps(claim, claims[index2]):
            if claim['id'] in ids:
                ids.remove(claim['id'])
            
            if claims[index2]['id'] in ids:
                ids.remove(claims[index2]['id'])
                
    
print(ids[0])
