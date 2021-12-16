import sys

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
        #print(f'Literal: {int(value,2)}')
    else:
        length_bit = line[index]
        index += 1

        if length_bit == '0':
            index += 15
        else:
            index += 11
    
    return index

versions = 0

line = input().rstrip()
line = f'{int(line,16):0{len(line)*4}b}'
index = 0
length = len(line)

while index >= 0 and index < length - 8:
    index = parse_packet(index, line)
    
print(versions)
