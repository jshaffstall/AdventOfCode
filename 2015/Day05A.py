import sys

total = 0
vowels = 'aeiou'
forbidden = ['ab', 'cd', 'pq', 'xy']

for line in sys.stdin:
    if line.strip() == '-1':
        break
    
    num_vowels = len([r for r in line if r in vowels])
    num_forbidden = len([r for r in forbidden if r in line])
    num_doubled = len([r for i,r in enumerate(line) if i<len(line)-1 and line[i+1]==r])
    
    total += 1 if num_vowels >= 3 and num_doubled > 0 and num_forbidden == 0 else 0
    
print(total)
