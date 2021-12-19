import sys
from collections import Counter

def between(a, b, c):
    return a >= min(b,c) and a <= max(b,c)

wires = []

for line in sys.stdin:
    line = line.rstrip()
    
    x = 0
    y = 0
    
    wire = []
    wire.append((x, y))
    
    for direction in line.split(','):
        distance = int(direction[1:])
        
        if direction[0]=='U':
            y += distance

        if direction[0]=='D':
            y -= distance

        if direction[0]=='L':
            x -= distance

        if direction[0]=='R':
            x += distance

        wire.append((x, y))
        
    wires.append(wire)
    
    if len(wires) == 2:
        break

wire1 = wires[0]
wire2 = wires[1]
intersections = []

for i1 in range(1, len(wire1)):
    for i2 in range(1, len(wire2)):
        w1vertical = wire1[i1-1][0] == wire1[i1][0]
        w1horizontal = wire1[i1-1][1] == wire1[i1][1]
        w2vertical = wire2[i2-1][0] == wire2[i2][0]
        w2horizontal = wire2[i2-1][1] == wire2[i2][1]
        
        if (w1vertical and w2vertical) or (w1horizontal and w2horizontal):
            continue
        
        if w1vertical:
            if between(wire1[i1-1][0], wire2[i2-1][0], wire2[i2][0]):
                if between(wire2[i2-1][1], wire1[i1-1][1], wire1[i1][1]):
                    intersections.append((wire1[i1-1][0], wire2[i2-1][1]))
            
        if w1horizontal:
            if between(wire1[i1-1][1], wire2[i2-1][1], wire2[i2][1]):
                if between(wire2[i2-1][0], wire1[i1-1][0], wire1[i1][0]):
                    intersections.append((wire2[i2-1][0], wire1[i1-1][1]))

if (0,0) in intersections:
    intersections.remove((0,0))
closest = min(intersections, key=lambda r: abs(r[0])+abs(r[1]))
print(abs(closest[0])+abs(closest[1]))

