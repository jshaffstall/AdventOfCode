import sys

def is_valid(first, second, third):
    return first+second>third and first+third>second and second+third>first

count = 0
numbers = {}
rows = 0

for line in sys.stdin:
    line = line.strip()
    
    if line == '-1':
        break
    
    first,second,third = [int(r) for r in line.split(' ') if r]
    numbers[(rows,0)] = first
    numbers[(rows,1)] = second
    numbers[(rows,2)] = third
    
    rows += 1
    
for row in range(0, rows, 3):
    for col in range(3):
        if is_valid(numbers[(row, col)], numbers[(row+1, col)], numbers[(row+2, col)]):
            count += 1
        
print(count)

