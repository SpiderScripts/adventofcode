f = open("05input.txt",'r')
#f = open("05sample.txt",'r')

data = f.readlines()

stacks = [[],[],[],[],[],[],[],[],[]]
#stacks = [[],[],[]]
line = 0

for i in data[7::-1]:
#for i in data[2::-1]:
    for x in range(9):
#    for x in range(3):
        box = i[4*x:4*x+3]
        if box != "   ":
            stacks[x].append(box)

for i in data[10:]:
#for i in data[5:]:
    ins = i.strip().split(" ")
    num = int(ins[1])
    start = int(ins[3])-1
    end = int(ins[5])-1
    length = len(stacks[start])
    move = stacks[start][length-num:]
    keep = stacks[start][:length-num]
    new = stacks[end] + move
    stacks[start] = keep
    stacks[end] = new

print(stacks)
