f = open("03input.txt",'r')

data = f.readlines()

score = 0
bag = 0
bags = []

#A-Z = 65-90
#a-z = 97-122

for i in data:
    bags.append(i.strip())
    bag += 1
    if bag == 3:
        dup = set(bags[0]).intersection(bags[1],bags[2])
        char = dup.pop()
        print(char)
        if char < "a":
            val = ord(char) - 38
        else:
            val = ord(char) - 96
        score += val
        bag = 0
        bags = []

print(score)
