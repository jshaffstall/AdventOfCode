import sys

sum = 0

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break

    numbers = [int(r) for r in line.split('\t')]
    
    for number in numbers:
        for number2 in numbers:
            if number2 == number:
                continue
            
            if number//number2 == number/number2:
                sum += number//number2
                break
        
print(sum)
