import sys

count_twos = 0
count_threes = 0

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break

    freq = {}
    
    for c in line:
        freq[c] = freq[c]+1 if c in freq else 1
    
    found_two = False
    found_three = False
    
    for c in freq:
        if freq[c] == 2 and not found_two:
            count_twos += 1
            found_two = True
            
        if freq[c] == 3 and not found_three:
            count_threes += 1
            found_three = True
            
print(count_twos*count_threes)

