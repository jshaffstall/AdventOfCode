import sys

lines = []
current = 5
code = ''

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break

    for c in line:
        if c == 'U':
            if current > 3:
                current -= 3
        
        if c == 'L':
            if current-1 not in (0, 3, 6):
                current -= 1
        
        if c == 'D':
            if current < 7:
                current += 3
        
        if c == 'R':
            if current+1 not in (4, 7, 10):
                current += 1
        
    code += str(current)
    
print(code)

