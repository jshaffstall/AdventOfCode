# This was seriously annoying!  And not in a fun to solve way.

import sys

target = int(input())
current = 3
index = 2

while True:
    if current*current == target:
        break
    
    if (current+2)*(current+2) > target:
        break
    
    current += 2
    index += 1

# row and column of the last lower right corner
# on the way to the target number
col = (current)-index
row = -col
row_dir = 1
col_dir = 0
distance = 0
side_length = (current)

current = (current)*(current)

if current < target:
    col += 1
    current += 1
    
    while current < target:
        if distance == side_length:
            row_dir = 0
            col_dir = -1
        if distance == side_length+(side_length+1):
            row_dir = -1
            col_dir = 0
        if distance == (side_length+1)*2+side_length:
            row_dir = 0
            col_dir = 1
            
        row += row_dir
        col += col_dir
        current += 1
        distance += 1
        print(distance, side_length, current, row, col)

print(abs(row)+abs(col))    

