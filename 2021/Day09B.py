import sys

def is_low_point(row, col):
    curr = lines[row][col]
    
    for r in range(row-1, row+2):
        if r < 0 or r >= len(lines):
            continue
        
        for c in range(col-1, col+2):
            if c < 0 or c >= length or (r == row and c == col):
                continue
            
            if lines[r][c] <= curr:
                return False
            
    return True

def calc_basin_size(row, col, visited):
    if row < 0 or row >= len(lines) or col < 0 or col >= length:
        return 0
    
    if lines[row][col] == '9':
        return 0
    
    if (row, col) in visited:
        return 0
    
    visited[(row, col)] = True
    return 1 + calc_basin_size(row-1,col, visited) + calc_basin_size(row+1,col, visited) + calc_basin_size(row,col-1, visited) + calc_basin_size(row,col+1, visited)

def get_basin_size(row, col):
    if is_low_point(row, col):
        return calc_basin_size(row, col, {})
    
    return 0

lines = []
length = 0

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break

    lines.append(line)
    length = len(line)

row = 0
sizes = []

for row in range(len(lines)):
    for col in range(length):
        sizes.append(get_basin_size(row, col))
        
sizes.sort()
sizes.reverse()
print(sizes[0]*sizes[1]*sizes[2])
            
