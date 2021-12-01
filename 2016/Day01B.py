# A bit brute force, but gets the job done

import sys

def check_position():
    if (x, y) in positions:
        distance = abs(x)+abs(y)
        print(distance)
        sys.exit()
 
    positions[(x, y)] = 1
    
def north(distance):
    global y
    global current
    
    for i in range(distance):
        y += 1
        check_position()
        
    current = 'N'
    
def east(distance):
    global x
    global current
    
    for i in range(distance):
        x += 1
        check_position()
        
    current = 'E'

def south(distance):
    global y
    global current
    
    for i in range(distance):
        y -= 1
        check_position()
        
    current = 'S'
    
def west(distance):
    global x
    global current
    
    for i in range(distance):
        x -= 1
        check_position()
        
    current = 'W'

facings = {
    'N': {
        'R': east,
        'L': west
    },
    'S': {
        'R': west,
        'L': east
    },
    'E': {
        'R': south,
        'L': north
    },
    'W': {
        'R': north,
        'L': south
    },
}

directions = input()
directions = directions.split(',')

x = 0
y = 0
current = 'N'
positions = {}

for direction in directions:
    direction = direction.strip()
    facings[current][direction[0]](int(direction[1:]))
    
    
