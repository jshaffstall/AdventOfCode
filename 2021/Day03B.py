import sys
import copy

def calc_rates(lines):
    rates = []

    for line in lines:
        index = 0
        
        for c in line:
            if index == len(rates):
                rates.append({'0': 0, '1': 0})
            
            rates[index][c] += 1
            index += 1
            
    return rates
    
lines = []

for line in sys.stdin:
    line = line.strip()
    
    if line == '-1':
        break

    lines.append(line)
    
lines2 = copy.deepcopy(lines)
index = 0

while len(lines) > 1:
    rates = calc_rates(lines)
    
    common = '1'
    if rates[index]['0'] > rates[index]['1']:
        common = '0'
        
    to_delete = []
    
    for line in lines:
        if line[index] != common:
            to_delete.append(line)
            
    for deletion in to_delete:
        lines.remove(deletion)
        
    index += 1
   
oxy = int(lines[0], 2)
lines = lines2
index = 0

while len(lines) > 1:
    rates = calc_rates(lines)
    
    common = '0'
    if rates[index]['0'] > rates[index]['1']:
        common = '1'
        
    to_delete = []
    
    for line in lines:
        if line[index] != common:
            to_delete.append(line)
            
    for deletion in to_delete:
        lines.remove(deletion)
        
    index += 1

co2 = int(lines[0], 2)

print(oxy*co2)
