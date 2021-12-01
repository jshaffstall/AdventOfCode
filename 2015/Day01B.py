import sys

directions = input()

current = 0
index = 1

for direction in directions:
    if direction == '(':
        current += 1
        
    if direction == ')':
        current -= 1
        
    if current == -1:
        print(index)
        sys.exit()
        
    index += 1
