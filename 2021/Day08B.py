# This was not the one to do the day after a migraine. 
# I normally love backtracking, but with my foggy brain
# I got so much wrong on the track to the right answer.  
# I'm convinced it's way more complicated than it needs to be.

import sys
import copy

def remove_except(segments, which, display):
    for c in ('a', 'b', 'c', 'd', 'e', 'f', 'g'):
        if c in which:
            segments[c] = [r for r in segments[c] if r in display]
        else:
            segments[c] = [r for r in segments[c] if r not in display]
        
def good_fit(segments, which, display):
    display = [c for c in display]
    matched = []
    
    for c in display:
        for segment in which:
            if c in segments[segment] and segment not in matched:
                matched.append(segment)
                
    return len(matched) == len(display)
            
def solve(segments, scrambled):
    # Base case
    if not scrambled:
        return segments
    
    display = scrambled[0]
    
    # Recursive cases

    # 8
    if len(display) == 7:
        segments2 = copy.deepcopy(segments)
        # Everything is lit, nothing to remove
        segments2 = solve(segments2, scrambled[1:])
        if segments2:
            return segments2
    
    if len(display) == 5:
        # 2
        if good_fit(segments, 'acdeg', display):
            segments2 = copy.deepcopy(segments)
            remove_except(segments2, 'acdeg', display)
            segments2 = solve(segments2, scrambled[1:])
            if segments2:
                return segments2
        
        # 3
        if good_fit(segments, 'acdfg', display):
            segments2 = copy.deepcopy(segments)
            remove_except(segments2, 'acdfg', display)
            segments2 = solve(segments2, scrambled[1:])
            if segments2:
                return segments2

        # 5
        if good_fit(segments, 'abdfg', display):
            segments2 = copy.deepcopy(segments)
            remove_except(segments2, 'abdfg', display)
            segments2 = solve(segments2, scrambled[1:])
            if segments2:
                return segments2
            
    if len(display) == 6:
        # 0
        if good_fit(segments, 'abcefg', display):
            segments2 = copy.deepcopy(segments)
            remove_except(segments2, 'abcefg', display)
            segments2 = solve(segments2, scrambled[1:])
            if segments2:
                return segments2
        
        # 6
        if good_fit(segments, 'abdefg', display):
            segments2 = copy.deepcopy(segments)
            remove_except(segments2, 'abdefg', display)
            segments2 = solve(segments2, scrambled[1:])
            if segments2:
                return segments2
            
        # 9  
        if good_fit(segments, 'abcdfg', display):
            segments2 = copy.deepcopy(segments)
            remove_except(segments2, 'abcdfg', display)
            segments2 = solve(segments2, scrambled[1:])
            if segments2:
                return segments2
            
    return None

def parse(targets, segments):
    result = ''
    values = [r[0] for r in list(segments.values())]
    keys = list(segments.keys())
    digits = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9'
    }
    
    for target in targets:
        temp = []
        for c in target:
            temp.append(keys[values.index(c)])
        temp.sort()            
        temp = ''.join(temp)
        result += digits[temp]
        
    return int(result)

result = 0

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break

    segments = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': []}
    
    for segment in segments:
        segments[segment] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        
    scrambled, target = [r.strip().split(' ') for r in line.split('|')]
    
    # Take care of the easy ones first
    for display in scrambled:
        # 1
        if len(display) == 2:
            remove_except(segments, 'cf', display)
        
        # 7
        if len(display) == 3:
            remove_except(segments, 'acf', display)
           
        # 4
        if len(display) == 4:
            remove_except(segments, 'bcdf', display)
        
    scrambled = [r for r in scrambled if len(r)>4]
    
    # Now do the backtracking for the rest
    segments = solve(segments, scrambled)
    result += parse(target, segments)
        
print(result)
