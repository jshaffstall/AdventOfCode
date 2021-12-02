# Not there yet, still needs work

import sys

def process_op(front, wire, wires):
    if 'NOT' in front:
        front = front[4:].strip()
        
        if front in wires:
            wires[wire] = ~wires[front]
            return True
        
    elif 'AND' in front:
        first, second = front.split('AND')
        first = first.strip()
        second = second.strip()
        
        first_value = None
        second_value = None
        
        if first in wires:
            first_value = wires[first]
        elif first.isdigit():
            first_value = int(first)
        
        if second in wires:
            second_value = wires[second]
        elif second.isdigit():
            second_value = int(second)
        
        if first_value is not None and second_value is not None:
            wires[wire] = first_value & second_value
            return True
    
    elif 'OR' in front:
        first, second = front.split('OR')
        first = first.strip()
        second = second.strip()
        
        first_value = None
        second_value = None
        
        if first in wires:
            first_value = wires[first]
        elif first.isdigit():
            first_value = int(first)
        
        if second in wires:
            second_value = wires[second]
        elif second.isdigit():
            second_value = int(second)
        
        if first_value is not None and second_value is not None:
            wires[wire] = first_value | second_value
            return True
    
    elif 'LSHIFT' in front:
        first, second = front.split('LSHIFT')
        first = first.strip()
        second = second.strip()
        
        if first in wires:
            wires[wire] = wires[first] << int(second)
            return True
        
    elif 'RSHIFT' in front:
        first, second = front.split('RSHIFT')
        first = first.strip()
        second = second.strip()
        
        if first in wires:
            wires[wire] = wires[first] >> int(second)
            return True
    else:
        if front in wires:
            wires[wire] = wires[front]
            return True
        
    return False

lines = []

for line in sys.stdin:
    if line.strip() == '-1':
        break

    lines.append(line)
    
wires = {}
index = 0
count = 0

while len(lines) > 0:
    front, wire = lines[index].split('->')
    wire = wire.strip()
    front = front.strip()
    
    if front.isdigit():
        wires[wire] = int(front)
        del lines[index]
    elif process_op(front, wire, wires):
        del lines[index]
    else:
        index = index + 1
        
    if len(lines) > 0:
        index %= len(lines)
        
print(wires['a'])
