import sys
code = 0
characters = 0

for line in sys.stdin:
    line = line.strip()
    
    if line == '-1':
        break
    
    code += len(line)
    
    while True:
        index = line.find('\\')
        
        if index == -1:
            break
        
        characters += 2
        line = line[:index]+line[index+1:]

    while True:
        index = line.find('"')
        
        if index == -1:
            break
        
        characters += 2
        line = line[:index]+line[index+1:]

    characters += len(line)+2

print(characters-code)
