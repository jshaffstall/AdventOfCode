# Ugh, regular expressions!

import sys
import re

total = 0

for line in sys.stdin:
    if line.strip() == '-1':
        break
    
    expression = r'([a-z])([a-z])[a-z]*\1\2'
    doubled = len(re.findall(expression, line))
    
    expression = r'([a-z]).\1'
    repeated = len(re.findall(expression, line))
    
    total += 1 if doubled > 0 and repeated > 0 else 0
    
print(total)
