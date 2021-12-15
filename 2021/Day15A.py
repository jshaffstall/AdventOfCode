# Definitely not the most efficient approach
# but it got the job done for part 1, at least

import sys
from queue import PriorityQueue

def add_to_queue(queue, cost, x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return
    
    if (x,y,cost+grid[(x,y)]) in visited:
        return
    
    if mincost and cost + grid[(x,y)] >= mincost:
        return
    
    visited[(x,y,cost+grid[(x,y)])] = grid[(x,y)]

    queue.put((cost+grid[(x,y)], x, y))
    
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

queue = PriorityQueue()
queue.put((0, 0, 0))
visited = {}

mincost = None

while not queue.empty():
    cost,x,y = queue.get()
    
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
