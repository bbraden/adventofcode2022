items = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# items list aids in finding the score of a character using items.index(CHARACTER)
def part1(file):
    total = 0 # sets total
    def get(value): # gets common character between a string split in half
        for i in list(set(value[:len(value)//2])&set(value[len(value)//2:])):return i # checks for shared characters in the value split in half and returns what is found
    with open(file, 'r') as o:  # opens input file
        for line in o: total += items.index(get(line.strip())) # for each line in the input, it uses get() to find the score of the shared character
    print(f'part1---> {total}') # prints out final score for part 1
def part2(file):
    def getCommonCharacter(s1,s2,s3): # will get common character between 3 strings
        common = '' # sets blank string
        for i in list(set(s1)&set(s2)): common += i # adds all common characters in the first and second string to the blank string
        return [i for i in list(set(s3)&set(common))][0] # returns the shared characters between the string of shared characters and the third string

    total = 0 # sets total
    with open(file, 'r') as p: # opens input file
        count = 0 # creates count variable which aids in choosing the correct lines
        group = [line.strip() for line in p] # puts all lines into one list variable
        for i in range(int(len(group)/3)): # runs for every 3 lines in input file
            total += items.index(getCommonCharacter(group[count], group[count + 1], group[count + 2])) # adds score of the common character between the three selected lines to total
            count += 3 # adds 3 to count for next iteration so the lines are the next 3
        print(f'part2---> {total}') # prints out final answer for part 2
        
part1('input.txt')
part2('input.txt')
