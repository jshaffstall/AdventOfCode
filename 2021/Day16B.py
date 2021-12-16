# Requires Python 3.8 or better, for the use of math.prod

import sys
import math

def parse_packet(index, line):
    global versions
    
    version = line[index:index+3]
    versions += int(version,2)

    index += 3
    
    type_id = int(line[index:index+3],2)

    index += 3

    if type_id == 4:
        value = ''
        while True:
            value += line[index+1:index+5]

            index += 5
            if line[index-5] == '0':
                break
            
        value = int(value,2)
    else:
        length_bit = line[index]
        index += 1
        bits = None
        packets = None
        
        if length_bit == '0':
            bits = int(line[index:index+15],2)
            index += 15
        else:
            packets = int(line[index:index+11],2)
            index += 11
        
        values = []
        while True:
            if bits is not None and bits <= 0:
                break
            
            if packets is not None and packets <= 0:
                break
            
            result,value = parse_packet(index, line)
            result = result - index
            index += result
            values.append(value)
            
            if packets:
                packets -= 1
                
            if bits:
                bits -= result
                
        if type_id == 0:
            value = sum(values)
        
        if type_id == 1:
            value = math.prod(values)
        
        if type_id == 2:
            value = min(values)
        
        if type_id == 3:
            value = max(values)
            
        if type_id == 5:
            if values[0] > values[1]:
                value = 1
            else:
                value = 0
        
        if type_id == 6:
            if values[0] < values[1]:
                value = 1
            else:
                value = 0
                
        if type_id == 7:
            if values[0] == values[1]:
                value = 1
            else:
                value = 0
                
    return index,value

versions = 0

line = input().rstrip()
line = f'{int(line,16):0{len(line)*4}b}'
index = 0
length = len(line)

while index >= 0 and index < length - 8:
    index,value = parse_packet(index, line)
    
print(value)
