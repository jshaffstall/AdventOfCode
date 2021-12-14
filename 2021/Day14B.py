import sys
from collections import Counter

template = []
insertions = []

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break
    
    if not line:
        continue
    
    if not '->' in line:
        template = [c for c in line.strip()]
    else:
        pair,substitution = [r.strip() for r in line.split('->')]
        insertions.append((pair,substitution))
       
pairs = Counter()
elements = Counter()
elements.update(template[0])

for index in range(1, len(template)):
    elements.update(template[index])
    pairs.update([''.join([template[index-1], template[index]])])

for count in range(40):
    adjustments = pairs.copy()
    
    for insertion in insertions:
        if insertion[0] in pairs:
            elements[insertion[1]] += pairs[insertion[0]]
            
            adjustments[insertion[0][0]+insertion[1]] += pairs[insertion[0]]
            adjustments[insertion[1]+insertion[0][1]] += pairs[insertion[0]]
            adjustments[insertion[0]] -= pairs[insertion[0]]

    pairs = adjustments
    
print(max(elements.values())-min(elements.values()))
            
