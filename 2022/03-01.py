f = open("03input.txt",'r')

data = f.readlines()

score = 0

#A-Z = 65-90
#a-z = 97-122


for i in data:
    left = i[0:int(len(i)/2)]
    right = i[int(len(i)/2):]
    dup = set(left).intersection(right)
    char = dup.pop()
    if char < "a":
        val = ord(char) - 38
    else:
        val = ord(char) - 96
    score += val    

print(score)
