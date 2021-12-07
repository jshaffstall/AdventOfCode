import sys

sum = 0

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break

    numbers = [int(r) for r in line.split('\t')]
    sum += max(numbers)-min(numbers)
        
print(sum)
