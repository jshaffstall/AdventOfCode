# This was an annoying part 2!

import sys

keypad = [
    ['', '' , '' , '' , '' , '' , ''],
    ['', '' , '' , '1', '' , '' , ''],
    ['', '' , '2', '3', '4', '' , ''],
    ['', '5', '6', '7', '8', '9', ''],
    ['', '' , 'A', 'B', 'C', '' , ''],
    ['', '' , '' , 'D', '' , '' , ''],
    ['', '' , '' , '' , '' , '' , ''],
    ]

row = 3
col = 1
code = ''

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break

    for c in line:
        if c == 'U':
            if keypad[row-1][col]:
                row -= 1
        
        if c == 'L':
            if keypad[row][col-1]:
                col -= 1
        
        if c == 'D':
            if keypad[row+1][col]:
                row += 1
        
        if c == 'R':
            if keypad[row][col+1]:
                col += 1
        
    code += keypad[row][col]
    
print(code)

