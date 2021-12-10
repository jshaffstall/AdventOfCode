import sys

matches = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

scoring = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


scores = []

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break

    score = 0
    stack = []
    corrupted = False
    
    for c in line:
        if c in ('(', '[', '{', '<'):
            stack.append(c)
            
        if c in (')', ']', '}', '>'):
            opening = stack[-1]
            del stack[-1]
            
            if c != matches[opening]:
                corrupted = True
                
    if corrupted:
        continue
    
    if len(stack) == 0:
        continue
    
    while len(stack) > 0:
        opening = stack[-1]
        del stack[-1]
        
        score = score * 5 + scoring[opening]
        
    scores.append(score)

scores.sort()
print(scores[len(scores)//2])

