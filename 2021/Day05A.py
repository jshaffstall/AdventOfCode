import sys
import math

lines = []

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break

    lines.append(line)
    
spaces = {}

for line in lines:
    start, end = line.split('->')
    startx, starty = [int(r) for r in start.split(',')]
    endx, endy = [int(r) for r in end.split(',')]
    
    if startx != endx and starty != endy:
        continue
    
    stepx = 0 if startx == endx else math.copysign(1, endx-startx)
    stepy = 0 if starty == endy else math.copysign(1, endy-starty)
    
    while True:
        if (startx, starty) not in spaces:
            spaces[(startx, starty)] = 0
            
        spaces[(startx, starty)] += 1
        
        if startx == endx and starty == endy:
            break
        
        startx += stepx
        starty += stepy
    
total = 0    
for space in spaces:
    if spaces[space] > 1:
        total += 1
        
print(total)
