items = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def part1(file):
    total = 0
    def get(value):
        firstpart, secondpart = value[:len(value)//2], value[len(value)//2:]
        for i in list(set(firstpart)&set(secondpart)):
            return i
    with open(file, 'r') as o:
        for line in o: total += items.index(get(line.strip()))
        print(f'part1---> {total}')
def part2(file):
    def getCommonCharacter(s1,s2,s3):
        common = ''
        commonList = []
        a=list(set(s1)&set(s2))
        for i in a:
            common+=i
        a=list(set(s3)&set(common))
        for i in a:
            commonList.append(i)
        for c in commonList:
            if c not in s1:
                commonList.remove(c)
            if c not in s2:
                commonList.remove(c)
            if c not in s3:
                commonList.remove(c)
        return commonList[0]

    total = 0
    with open(file, 'r') as p:
        count = 0
        group = []
        for line in p:
            group.append(line.strip())
        for i in range(int(len(group)/3)):
            total += items.index(getCommonCharacter(group[count], group[count + 1], group[count + 2]))
            count += 3
        print(f'part2---> {total}')
part1('input.txt')
part2('input.txt')
