# This one was just annoying, since it didn't add anything interesting
# to the problem.

import sys

previous = None
increases = 0

elves = []
total = 0

for line in sys.stdin:
    line = line.replace('\n', '')

    if not line or line == '-1':
        elves.append(total)
        total = 0
        
        if line == '-1':
            break
        
        continue
    
    current = int(line)
    
    total += current    
    
total = 0
total += max(elves)
elves.remove(max(elves))
total += max(elves)
elves.remove(max(elves))
total += max(elves)

print(total)

