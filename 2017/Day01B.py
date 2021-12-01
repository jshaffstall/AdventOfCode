import sys

numbers = input()

total = 0
length = len(numbers)

for index in range(length):
    if numbers[index] == numbers[(index+length//2)%length]:
        total += int(numbers[index])
        
print(total)

