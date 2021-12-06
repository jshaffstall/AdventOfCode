# The part one brute force approach was much too slow for this version,
# so switching to a dictionary counting the number of each digit
# was needed to keep this running in a reasonable amount of time

import sys

line = input()
numbers = {
    0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0
}

for r in line.split(','):
    r = int(r)
    numbers[r] += 1
    
day = 0

while day < 256:
    num_zeroes = numbers[0]
    numbers = {i:numbers[i+1] for i in range(8)}
    numbers[8] = num_zeroes
    numbers[6] += num_zeroes
    day += 1
    
print(sum([numbers[i] for i in range(9)]))

