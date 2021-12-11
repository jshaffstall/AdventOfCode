import sys

line = input()
original = [int(r) for r in line.split(',')]

for noun in range(99):
    for verb in range(99):
        numbers = original.copy()
        numbers[1] = noun
        numbers[2] = verb
        index = 0
        
        while True:
            if numbers[index] == 1:
                numbers[numbers[index+3]] = numbers[numbers[index+1]]+numbers[numbers[index+2]]
            elif numbers[index] == 2:
                numbers[numbers[index+3]] = numbers[numbers[index+1]]*numbers[numbers[index+2]]
            elif numbers[index] == 99:
                break
            
            index += 4
            
        if numbers[0] == 19690720:
            print(100*noun+verb)
            sys.exit()
