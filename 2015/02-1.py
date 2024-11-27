f = open("02input.txt",'r')

data = f.readlines()

total = 0

for i in data:
    val = i.split("x")
    ival = [int(val[0]),int(val[1]),int(val[2])]
    ival.sort()
    l = int(val[0])
    w = int(val[1])
    h = int(val[2])
    sa = 2*(l*w+l*h+h*w)+ival[0]*ival[1]
    total += sa

print(total)

total = 0

for i in data:
    val = i.split("x")
    ival = [int(val[0]),int(val[1]),int(val[2])]
    ival.sort()
    l = int(val[0])
    w = int(val[1])
    h = int(val[2])
    length = 2*(ival[0]+ival[1]) + l*w*h
    total += length

print(total)
