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

def get_risk_level(row, col):
    if is_low_point(row, col):
        return int(lines[row][col])+1
    
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
sum = 0

for row in range(len(lines)):
    for col in range(length):
        sum += get_risk_level(row, col)
        
print(sum)
            
