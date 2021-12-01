import sys
import hashlib

line = input().strip()
current = 1

while True:
    hash = hashlib.md5((line+str(current)).encode('utf-8')).hexdigest()
    
    if hash.startswith('000000'):
        print(current)
        sys.exit()
        
    current += 1
