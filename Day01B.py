import sys

numbers = []

for line in sys.stdin:
    current = int(line)
    
    if current == -1:
        break
    
    numbers.append(current)

previous = numbers[0]+numbers[1]+numbers[2]
increases = 0

for index in range(1, len(numbers)-2):
    current = numbers[index]+numbers[index+1]+numbers[index+2]
    
    if current > previous:
        increases += 1
        
    previous = current
    
print(increases)
