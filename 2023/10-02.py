f = open("10input.txt",'r')

data = f.readlines()

'''
data = ["..F7.",
".FJ|.",
"SJ.L7",
"|F--J",
"LJ..."]
'''
'''
data = [".....",
".S-7.",
".|.|.",
".L-J.",
"....."]
'''

height = len(data)
width = len(data[0])

grid = {}
gridv = []

thisrow = 0
for i in data:
    gridv.append(list(i))
    thiscol = 0
    row = list(i)
    for col in row:
        gridref = (thisrow,thiscol)
        if col == "|":
            link = [(thisrow-1,thiscol),(thisrow+1,thiscol)]
        elif col == "-":
            link = [(thisrow,thiscol-1),(thisrow,thiscol+1)]
        elif col == "J":
            link = [(thisrow-1,thiscol),(thisrow,thiscol-1)]
        elif col == "L":
            link = [(thisrow-1,thiscol),(thisrow,thiscol+1)]
        elif col == "F":
            link = [(thisrow+1,thiscol),(thisrow,thiscol+1)]
        elif col == "7":
            link = [(thisrow+1,thiscol),(thisrow,thiscol-1)]
        elif col == ".":
            link = []
        elif col == "S":
            link = []
            start = gridref
        grid[gridref] = link
        thiscol += 1
    thisrow += 1

# work out what pipe is under S
froms = []
x = list(grid.values())
for i in range(len(grid)):
    if start in x[i]:
        froms.append(list(grid.keys())[i])
grid[start] = froms

# figure out the whole path from S
dist = 0
flag = True
current = start
visited = [start]
while flag:
    connected = grid[current]
    dist += 1
    if connected[0] not in visited:
        visited.append(connected[0])
        current = connected[0]
    elif connected[1] not in visited:
        visited.append(connected[1])
        current = connected[1]
    else:
        flag = False
        
for i in grid:
    if i not in visited:
        gridv[i[0]][i[1]] = " "

x = 281
y = 281
biggrid = []
for i in range(x):
    biggrid.append([])
    for j in range(y):
        biggrid[i].append("x")

def grow(x):
    return [2*x[0]+1,2*x[1]+1]
    
def mid(x,y):
    return [(x[0]+y[0])//2,(x[1]+y[1])//2]

for i in grid:
    if i in visited:
        j = grow(i)
        a = mid(j,grow(grid[i][0]))
        b = mid(j,grow(grid[i][1]))
        biggrid[j[0]][j[1]] = "P"
        biggrid[a[0]][a[1]] = "P"
        biggrid[b[0]][b[1]] = "P"
        
start = [0,0]
q = [start]
while q:
    this = q.pop()
    if biggrid[this[0]][this[1]] == "x":
        biggrid[this[0]][this[1]] = " "
        if this[0] > 0:
            q.append([this[0]-1,this[1]])
        if this[0] < x-1:
            q.append([this[0]+1,this[1]])
        if this[1] > 0:
            q.append([this[0],this[1]-1])
        if this[1] < y-1:
            q.append([this[0],this[1]+1])

count = 0
for i in range(1,x,2):
    for j in range(1,y,2):
        if biggrid[i][j] == "x":
            count += 1

print(count)