# Spent too much time on an annoying bug dealing
# with negative y values.  Otherwise, the same
# approach as with part 1.

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

count = 0
old_xv = 0

for xvv in range(maxx+1):
    for yvv in range(miny, abs(miny)+1):
        yv = yvv
        xv = xvv
        x = 0
        y = 0

        while True:
            if x > maxx or y < miny:
                break
            
            if in_target(x,y):
                count += 1
                break
                
            x += xv
            y += yv
            
            xv = xv - 1 if xv > 0 else xv + 1 if xv < 0 else 0
            yv -= 1

print(count)
