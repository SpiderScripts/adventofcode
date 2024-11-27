f = open("02-01input.txt",'r')

data = f.readlines()

score = 0

# A - rock, B - paper, C - scissors
# X - rock, Y - paper, Z - scissors
lookup = {"X":0,"Y":3,"Z":6,"AX":3,"AY":1,"AZ":2,"BX":1,"BY":2,"BZ":3,"CX":2,"CY":3,"CZ":1}

for i in data:
    them = i[0]
    us = i[2]
    score += lookup[us]
    score += lookup[them+us]

print(score)
