import sys

matches = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

scoring = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


score = 0

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break

    stack = []

    for c in line:
        if c in ('(', '[', '{', '<'):
            stack.append(c)
            
        if c in (')', ']', '}', '>'):
            opening = stack[-1]
            del stack[-1]
            
            if c != matches[opening]:
                score += scoring[c]
            
print(score)
