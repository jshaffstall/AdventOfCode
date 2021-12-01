import sys

line = input().strip()

total = 0
x = [0, 0]
y = [0, 0]
which = 0

houses = {(0,0): 1}

for direction in line:
    if direction == '<':
        x[which] -= 1

    if direction == '>':
        x[which] += 1

    if direction == '^':
        y[which] += 1

    if direction == 'v':
        y[which] -= 1
        
    if (x[which],y[which]) not in houses:
        houses[(x[which],y[which])] = 0
        
    houses[(x[which],y[which])] += 1
    which = (which+1)%2
        
print(len(houses.keys()))
