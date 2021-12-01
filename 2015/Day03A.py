import sys

line = input().strip()

total = 0
x = 0
y = 0
houses = {(0,0): 1}

for direction in line:
    if direction == '<':
        x -= 1

    if direction == '>':
        x += 1

    if direction == '^':
        y += 1

    if direction == 'v':
        y -= 1
        
    if (x,y) not in houses:
        houses[(x,y)] = 0
        
    houses[(x,y)] += 1
        
print(len(houses.keys()))
