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
        if which == 'y':
            distance = height+1
            for y in range(height-1, height//2, -1):
                distance -= 2
                for x in range(width):
                    if (y,x) in grid:
                        del grid[(y,x)]
                        grid[(y-distance,x)] = True
            
            height //= 2
        else:
            distance = width+1
            for x in range(width-1, width//2, -1):
                distance -= 2
                for y in range(height):
                    if (y,x) in grid:
                        del grid[(y,x)]
                        grid[(y,x-distance)] = True
            
            width //= 2
        
        # Part 1 only has us doing the first fold
        print(list(grid.values()).count(True))
        sys.exit()
    
