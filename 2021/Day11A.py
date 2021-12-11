import sys

def increase(numbers, row, col):
    if row < 0 or row >= rows or col < 0 or col >= columns:
        return
    
    numbers[(row,col)] += 1
    
def increase_adjacent(numbers, row, col):
    increase(numbers,row-1,col-1)
    increase(numbers,row-1,col)
    increase(numbers,row-1,col+1)
    increase(numbers,row,col-1)
    increase(numbers,row,col+1)
    increase(numbers,row+1,col-1)
    increase(numbers,row+1,col)
    increase(numbers,row+1,col+1)
    
numbers = {}
row = 0

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break
    
    columns = len(line)
    col = 0
    for c in line:
        numbers[(row,col)] = int(c)
        col += 1
        
    row += 1

rows = row

flashes = 0
for step in range(100):
    for row in range(rows):
        for col in range(columns):
            numbers[(row,col)] += 1
            
    flashed = []
    found_flash = True
                
    while found_flash:
        found_flash = False
        
        for row in range(rows):
            for col in range(columns):
                if numbers[(row,col)] > 9 and (row,col) not in flashed:
                    increase_adjacent(numbers, row, col)
                    flashes += 1
                    found_flash = True
                    flashed.append((row,col))
        
        
    for item in flashed:
        numbers[item] = 0
    
print(flashes)
