f = open("05input.txt",'r')
#f = open("05sample.txt",'r')

data = f.readlines()

stacks = [[],[],[],[],[],[],[],[],[]]
#stacks = [[],[],[]]
line = 0

for i in data[7::-1]:
#for i in data[2::-1]:
    for x in range(9):
        box = i[4*x:4*x+3]
        if box != "   ":
            stacks[x].append(box)

print(stacks)
print()

for i in data[10:]:
    ins = i.split(" ")
    num = int(ins[1])
    start = int(ins[3])-1
    end = int(ins[5])-1
    print(ins)
    for x in range(num):
        #print(stacks)
        if len(stacks[start]) == 1:
            move = stacks[start][len(stacks[start])-1]
            stacks[start] = []
        else:
            move = stacks[start].pop()
        if stacks[end] == []:
            #print(move)
            stacks[end] = [move]
        else:
            stacks[end].append(move)

print(stacks)
