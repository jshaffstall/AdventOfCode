import sys

lines = []
length = 0

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break

    lines.append(line)
    length = len(line)
    
for first in lines:
    for second in lines:
        diffs = 0
        
        for i in range(length):
            if first[i] != second[i]:
                diffs += 1
                
        if diffs == 1:
            temp = ''
            for i in range(length):
                if first[i] == second[i]:
                    temp += first[i]
            print(temp)
            sys.exit()
                
