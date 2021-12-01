import sys

total = 0

for line in sys.stdin:
    if line.strip() == '-1':
        break

    dimensions = [int(r) for r in line.strip().split('x')]

    one = dimensions[0]*dimensions[1]
    two = dimensions[0]*dimensions[2]
    three = dimensions[1]*dimensions[2]
    
    total += 2*one+2*two+2*three+min([one, two, three])
    
print(total)
