import sys
import math

def in_target(x,y):
    return x >= minx and x <= maxx and y >= miny and y <= maxy

line = input().rstrip()
prefix,rest = line.split(':')
xpart,ypart = rest.split(',')
_,xrange=xpart.split('=')
_,yrange=ypart.split('=')
minx,maxx = [int(r) for r in xrange.split('..')]
miny,maxy = [int(r) for r in yrange.split('..')]

highest = None

for xv in range(maxx):
    for yv in range(maxy, abs(miny)):
        temphighest = None
        x = 0
        y = 0

        while True:
            if not temphighest or y > temphighest:
                temphighest = y
                
            if x > maxx or y < maxy:
                break
            
            if in_target(x,y):
                break
                
            x += xv
            y += yv
            
            xv = xv - 1 if xv > 0 else xv + 1 if xv < 0 else 0
            yv -= 1

        if temphighest and (not highest or temphighest > highest):
            highest = temphighest
    
print(highest)
