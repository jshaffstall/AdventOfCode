import sys

total = 0

for line in sys.stdin:
    if line.strip() == '-1':
        break

    dimensions = [int(r) for r in line.strip().split('x')]
    dimensions.sort()
    
    one = 2*dimensions[0]+2*dimensions[1]
    two = dimensions[0]*dimensions[1]*dimensions[2]
    
    total += one+two
    
print(total)
