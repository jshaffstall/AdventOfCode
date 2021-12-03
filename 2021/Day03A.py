import sys

rates = []

for line in sys.stdin:
    line = line.strip()
    
    if line == '-1':
        break

    index = 0
    
    for c in line:
        if index == len(rates):
            rates.append({'0': 0, '1': 1})
        
        rates[index][c] += 1
        index += 1
        
gamma = ''
epsilon = ''

for rate in rates:        
    if rate['0'] > rate['1']:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
        
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma*epsilon)
