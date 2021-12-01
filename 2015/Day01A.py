import sys

directions = input()

current = 0

for direction in directions:
    if direction == '(':
        current += 1
        
    if direction == ')':
        current -= 1
        
print(current)
