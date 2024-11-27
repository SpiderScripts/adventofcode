f = open("02-01input.txt",'r')

data = f.readlines()

score = 0

# A - rock, B - paper, C - scissors
# X - rock, Y - paper, Z - scissors
lookup = {"X":1,"Y":2,"Z":3,"AX":3,"AY":6,"AZ":0,"BX":0,"BY":3,"BZ":6,"CX":6,"CY":0,"CZ":3}

for i in data:
    them = i[0]
    us = i[2]
    score += lookup[us]
    score += lookup[them+us]

print(score)
