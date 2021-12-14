import sys

template = ''
insertions = []

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break
    
    if not line:
        continue
    
    if not '->' in line:
        template = line
    else:
        pair,substitution = [r.strip() for r in line.split('->')]
        insertions.append((pair,substitution))
       
for count in range(10):
    new_template = template[0]
    for index in range(len(template)-1):
        pair = template[index:index+2]
        found = False
        
        for insertion in insertions:
            if insertion[0] == pair:
                new_template += insertion[1]+pair[1]
                found = True
        
        if not found:
            new_template += pair[1]
            
    template = new_template

counts = {}

for c in template:
    if c not in counts:
        counts[c] = 0
        
    counts[c] += 1
    
print(counts[max(counts, key=counts.get)]-counts[min(counts, key=counts.get)])

