with open('input.txt', 'r') as a: group = [line.strip() for line in a]
part = 1

def find(input):
    x=[]
    for i in input:
        if i not in x and input.count(i)>1: x.append(i)
    return True if (" ".join(x)) == '' else False

for i in range(2):
    for code in group:
        found = False ; count = 0 ; chars = ''
        while not found:
            for i in range(4 if part == 1 else 14): chars += code[i + count]
            if(find(chars)): print(f'part {part} --> {count + (4 if part == 1 else 14)}'); found = True
            else: count += 1 ; chars = ''
    part = 2
