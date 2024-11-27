f = open("10input.txt",'r')

data = f.readlines()

data = ["..F7.",
".FJ|.",
"SJ.L7",
"|F--J",
"LJ..."]

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
        
print(dist)

for i in grid:
    if i not in visited:
        gridv[i[0]][i[1]] = " "
        
for i in range(len(gridv)):
    gridv[i] = ("".join(gridv[i]))
    print(gridv[i])