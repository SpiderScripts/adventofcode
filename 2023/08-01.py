f = open("08input.txt",'r')

data = f.readlines()

'''
data = ["LR",
"",
"11A = (11B, XXX)",
"11B = (XXX, 11Z)",
"11Z = (11B, XXX)",
"22A = (22B, XXX)",
"22B = (22C, 22C)",
"22C = (22Z, 22Z)",
"22Z = (22B, 22B)",
"XXX = (XXX, XXX)"]
'''

nav = data[0].strip()

start = []
desert = {}

for i in data[2:]:
    desert[i[:3]] = [i[7:10],i[12:15]]
    if i[2] == "A":
        start.append(i[:3])

paths = []
loc = "AAA"
turn = 0
step = 0
flag = True

'''
# part 1
while loc != "ZZZ":
    step += 1
    if nav[turn] == "L":
        loc = desert[loc][0]
    else:
        loc = desert[loc][1]
    turn += 1
    if turn == len(nav):
        turn = 0

print("part 1",step)
'''

# part 2
print(start)
for loc in start:
    turn = 0
    step = 0
    while loc[2] != "Z":
        step += 1
        if nav[turn] == "L":
            loc = desert[loc][0]
        else:
            loc = desert[loc][1]
        turn += 1
        if turn == len(nav):
            turn = 0
    paths.append(step)
