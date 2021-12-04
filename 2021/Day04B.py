import sys

def mark_board(board, number):
    for row in range(5):
        for col in range(5):
            if board[(row, col)]['value'] == number:
                board[(row, col)]['marked'] = True

def display_stats(board, number):
    sum = 0
    for row in range(5):
        for col in range(5):
            if not board[(row, col)]['marked']:
                sum += int(board[(row, col)]['value'])
                
    print(sum*int(number))
    
    
def board_wins(board, number):
    for row in range(5):
        won = True
        for col in range(5):
            if not board[(row, col)]['marked']:
                won = False
                
        if won == True:
            #display_stats(board, number)
            return True

    for col in range(5):
        won = True
        for row in range(5):
            if not board[(row, col)]['marked']:
                won = False
                
        if won == True:
            #display_stats(board, number)
            return True
        
    return False

lines = []

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break

    lines.append(line)
    
numbers = lines[0].split(',')
boards = []
index = 2

while index < len(lines):
    board = {'won': False}
    for row in range(5):
        for col in range(5):
            space = lines[index+row][3*col:3*col+2].strip()
            board[(row,col)] = {'value': space, 'marked': False}
            
    boards.append(board)
    index += 6

num_won = 0
for number in numbers:
    for board in boards:
        if board['won']:
            continue
        
        mark_board(board, number)
        
        if board_wins(board, number):
            board['won'] = True
            num_won += 1
            if num_won == len(boards):
                display_stats(board, number)
