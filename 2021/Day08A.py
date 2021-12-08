# Took me an embarrasingly long time to realize we only
# needed to look in the target digits

import sys

count = 0

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break

    scrambled, target = [r.strip().split(' ') for r in line.split('|')]
    
    for display in target:
        count += 1 if len(display) in (2, 4, 3, 7) else 0


print(count)
