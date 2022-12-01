# CODE WRITTEN BY BRADEN https://github.com/bbraden

def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False

elf = []
elfList = []

collectingNumbers = False

with open('input.txt') as f:
    for line in f:
        if containsNumber(line):
            if collectingNumbers == False:
                elfList.append(sum(elf))
                elf.clear()
                collectingNumbers = True
                
            elf.append(int(line))
        else:
            collectingNumbers = False

# ANSWER ONE
print('**')
print(f'--> {max(elfList)}')
print('**')

# ANSWER TWO
answers = []

answers.append(max(elfList))
elfList.remove(max(elfList))

answers.append(max(elfList))
elfList.remove(max(elfList))

answers.append(max(elfList))

print('**')
print(f'--> {sum(answers)}')
print('**')