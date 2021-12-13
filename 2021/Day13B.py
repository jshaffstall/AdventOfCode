# I'm not at all happy with this one.  My mind
# immediately went to storing the grid, and 
# that complicated things.  I should have just
# stored a list of coordinates, and manipulated
# those directly, instead of trying to store
# the grid itself.

import sys

def print_grid(grid, width, height):
    print(width, height)
    
    for y in range(height):
        for x in range(width):
            if (y,x) in grid:
                print('#',end='')
            else:
                print('.',end='')
        print()
    
grid = {}
coords = True
height = 0
width = 0

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break
    
    if not line:
        coords = False
        continue
    
    if coords:
        x, y = [int(r) for r in line.split(',')]
        grid[(y,x)] = True
        height = y+1 if y >= height else height
        width = x+1 if x >= width else width
    else:
        line = line[11:]
        which,value = line.split('=')
        value = int(value)

        # Fold
        grid2 = {}
        for y,x in grid:
            if which == 'y':
                if y > value:
                    y = value*2-y
            else:
                if x > value:
                    x = value*2-x
            grid2[(y,x)] = True
            
        grid = grid2
        height = height//2 if which == 'y' else height
        width = width//2 if which == 'x' else width
        
print_grid(grid, width, height)
    
