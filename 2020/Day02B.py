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
    
    if password[low-1] == char and password[high-1] != char:
        valid += 1
            
    if password[low-1] != char and password[high-1] == char:
        valid += 1
        
print(valid)
