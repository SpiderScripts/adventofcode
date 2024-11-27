f = open("01-01input.txt",'r')

data = f.readlines()

big = 0
cur = 0

for i in data:
    if i == "\n":
        if cur > big:
            big = cur
        cur = 0
    else:
        cur += int(i)
