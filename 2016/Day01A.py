import sys

def north(distance):
    global y
    global current
    y += distance
    current = 'N'
    
def east(distance):
    global x
    global current
    x += distance
    current = 'E'

def south(distance):
    global y
    global current
    y -= distance
    current = 'S'
    
def west(distance):
    global x
    global current
    x -= distance
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

for direction in directions:
    direction = direction.strip()
    facings[current][direction[0]](int(direction[1:]))
    
distance = abs(x)+abs(y)
print(distance)
    
    
