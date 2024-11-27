f = open("01-01input.txt",'r')

data = f.readlines()

totals = []
cur = 0

for i in data:
    if i == "\n":
        totals.append(cur)
        cur = 0
    else:
        cur += int(i)

totals.sort()
