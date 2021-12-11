import sys

count = 0

for line in sys.stdin:
    line = line.strip()
    
    if line == '-1':
        break
    
    first,second,third = [int(r) for r in line.split(' ') if r]
    
    if first+second>third and first+third>second and second+third>first:
        count += 1
        
print(count)

