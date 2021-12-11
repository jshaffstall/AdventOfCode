import sys

valid = 0

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break
    
    policy,password = line.split(':')
    password = password.strip()
    
    valid_range,char = policy.split(' ')
    low,high = [int(r) for r in valid_range.split('-')]
    
    count = 0
    for c in password:
        if c == char:
            count += 1
            
    if count >= low and count <= high:
        valid += 1
        
print(valid)
