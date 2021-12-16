# The day 1 approach wasn't far off from being good for day 2, 
# just needed a little more discretion about adding
# duplicate items to the queue

import sys
from heapq import *

def print_grid():
    for row in range(height):
        for col in range(width):
            print(grid[(col,row)], end='')
            
        print()
        
def copy_grid(x1, y1, x2, y2):
    for x in range(width):
        for y in range(height):
            grid[(x2+x,y2+y)] = grid[(x1+x,y1+y)]+1 if grid[(x1+x,y1+y)] < 9 else 1

def add_to_queue(queue, cost, x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return
    
    if (x,y) in visited:
        return
    
    if mincost and cost + grid[(x,y)] >= mincost:
        return
    
    visited[(x,y)] = grid[(x,y)]

    need_to_add = True
    for index,item in enumerate(queue):
        if item[1] == x and item[2] == y:
            need_to_add = False
            if item[0] > cost+grid[(x,y)]:
                need_to_add = True
                found = True
                del queue[index]
                
            break
                 
    if need_to_add:                 
        heappush(queue, (cost+grid[(x,y)], x, y))
    
grid = {}
height = 0
y = 0

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break
    
    height += 1
    width = len(line)
    
    x = 0
    
    for c in line:
        grid[(x,y)] = int(c)
        x += 1
        
    y += 1

for row in range(5):
    if row > 0:
        copy_grid(0, height*(row-1), 0, height*row)
    
    for col in range(1, 5):
        copy_grid(width*(col-1), height*row, width*col, height*row)
        
width *= 5
height *= 5

queue = []
heappush(queue, (0, 0, 0))
visited = {}

mincost = None

while len(queue) != 0:
    cost,x,y = heappop(queue)
    
    if mincost and cost > mincost:
        continue
    
    if x == width-1 and y == height-1:
        if not mincost or cost < mincost:
            mincost = cost

        continue
    
    add_to_queue(queue, cost, x, y-1)
    add_to_queue(queue, cost, x, y+1)
    add_to_queue(queue, cost, x-1, y)
    add_to_queue(queue, cost, x+1, y)
            
print(mincost)            
    
