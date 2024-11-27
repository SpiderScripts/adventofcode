f = open("03input.txt",'r')

data = f.readlines()

'''
data = ["467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."]
'''
total = 0
numbers = []
numpos = {}
symbols = []
numid = 0

for i in range(len(data)):
    num = False
    thisnum = ""
    for j in range(len(data[0])):
        if data[i][j] == "\n":
            if num == True:
                numbers.append(int(thisnum))
                thisnum = ""
                numid += 1
        elif data[i][j] != ".":
            try:
                int(data[i][j])
                if num == False:
                    numpos[i,j] = numid
                    thisnum = data[i][j]
                    num = True
                else:
                    numpos[i,j] = numid
                    thisnum += data[i][j]
            except:
                if num == True:
                    numbers.append(int(thisnum))
                    thisnum = ""
                    numid += 1
                if data[i][j] == "*":
                    symbols.append([i,j])
                num = False
        else:
            if num == True:
                numbers.append(int(thisnum))
                thisnum = ""
                numid += 1
            num = False

for sym in symbols:
    x = sym[0]
    y = sym[1]
    valid = []
    if (x-1,y-1) in numpos:
        valid.append(numpos[x-1,y-1])
    if (x-1,y) in numpos:
        valid.append(numpos[x-1,y])
    if (x-1,y+1) in numpos:
        valid.append(numpos[x-1,y+1])
    if (x,y-1) in numpos:
        valid.append(numpos[x,y-1])
    if (x,y+1) in numpos:
        valid.append(numpos[x,y+1])
    if (x+1,y-1) in numpos:
        valid.append(numpos[x+1,y-1])
    if (x+1,y) in numpos:
        valid.append(numpos[x+1,y])
    if (x+1,y+1) in numpos:
        valid.append(numpos[x+1,y+1])
    if (len(set(valid)) == 2):
        inc = 1
        for val in set(valid):
            inc *= numbers[val]
        total += inc

print(total)
