import re

f = open("04input.txt",'r')

data = f.readlines()

'''
data = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]
'''

totals = []
stack = []
tracker = {}
cards = len(data)

def clean(line):
    line = re.sub(' +', ' ', line)
    num = int(line.split(":")[0].split(" ")[1])
    win = line.split(":")[1].split("|")[0].strip().split(" ")
    card = line.split(":")[1].split("|")[1].strip().split(" ")
    info = [[int(x) for x in win],[int(x) for x in card]]
    count = 0
    creates = []
    for x in info[0]:
        if x in info[1]:
            count += 1
            creates.append(num+count)
    tracker[num] = creates

for i in data:
    info = clean(i)
    totals.append(1)

for i in range(cards):
    this = totals[i]
    for j in tracker[i+1]:
        totals[j-1] += this

total = 0
for i in totals:
    total += i

print(total)
