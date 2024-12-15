data = open("15input.txt","r").read()

'''
data = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
'''

data = data.split("\n\n")
grid = [list(x) for x in data[0].splitlines()]
biggrid = []
move = data[1].replace("\n","")
m = {"<":[0,-1],
     ">":[0,1],
     "^":[-1,0],
     "v":[1,0]
     }


for i in range(len(grid)):
    biggrid.append([])
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            biggrid[i] += ["@","."]
            r = [i,j]
            rb = [i,j*2]
        elif grid[i][j] == "O":
            biggrid[i] += ["[","]"]
        else:
            biggrid[i] += [grid[i][j],grid[i][j]]

def disp(g):
    for i in range(len(g)):
        for j in range(len(g[0])):
            print(g[i][j],end="")
        print("")

def step(x,d):
    y = grid[x[0]+d[0]][x[1]+d[1]]
    if y == ".":
        grid[x[0]+d[0]][x[1]+d[1]] = grid[x[0]][x[1]]
        grid[x[0]][x[1]] = "."
        return True
    elif y == "O":
        if step([x[0]+d[0],x[1]+d[1]],d):
            grid[x[0]+d[0]][x[1]+d[1]] = grid[x[0]][x[1]]
            grid[x[0]][x[1]] = "."
            return True
        else:
            return False
    else:
        return False

def check(x,d):
    y = biggrid[x[0]+d[0]][x[1]+d[1]]
    if d[0] == 0: # easy mode
        if y == ".":
            return True
        elif y == "[" or y == "]":
            if check([x[0]+d[0],x[1]+d[1]],d):
                return True
            else:
                return False
        else:
            return False
    else:
        if y == ".":
            return True
        elif y == "[":
            if check([x[0]+d[0],x[1]+d[1]+1],d) and check([x[0]+d[0],x[1]+d[1]],d):
                return True
            else:
                return False
        elif y == "]":
            if check([x[0]+d[0],x[1]+d[1]-1],d) and check([x[0]+d[0],x[1]+d[1]],d):
                return True
            else:
                return False
        else:
            return False

def stepb(x,d):
    y = biggrid[x[0]+d[0]][x[1]+d[1]]
    if d[0] == 0: # easy mode
        if y == ".":
            return True
        elif y == "[" or y == "]":
            if stepb([x[0]+d[0],x[1]+d[1]],d):
                biggrid[x[0]+d[0]*2][x[1]+d[1]*2] = biggrid[x[0]+d[0]][x[1]+d[1]]
                biggrid[x[0]+d[0]][x[1]+d[1]] = "."
                return True
            else:
                return False
        else:
            return False
    else:
        if y == ".":
            return True
        elif y == "[":
            if stepb([x[0]+d[0],x[1]+d[1]+1],d) and stepb([x[0]+d[0],x[1]+d[1]],d):
                biggrid[x[0]+d[0]*2][x[1]+d[1]*2] = biggrid[x[0]+d[0]][x[1]+d[1]]
                biggrid[x[0]+d[0]*2][x[1]+d[1]*2+1] = biggrid[x[0]+d[0]][x[1]+d[1]+1]
                biggrid[x[0]+d[0]][x[1]+d[1]] = "."
                biggrid[x[0]+d[0]][x[1]+d[1]+1] = "."
                return True
            else:
                return False
        elif y == "]":
            if stepb([x[0]+d[0],x[1]+d[1]-1],d) and stepb([x[0]+d[0],x[1]+d[1]],d):
                biggrid[x[0]+d[0]*2][x[1]+d[1]*2] = biggrid[x[0]+d[0]][x[1]+d[1]]
                biggrid[x[0]+d[0]*2][x[1]+d[1]*2-1] = biggrid[x[0]+d[0]][x[1]+d[1]-1]
                biggrid[x[0]+d[0]][x[1]+d[1]] = "."
                biggrid[x[0]+d[0]][x[1]+d[1]-1] = "."
                return True
            else:
                return False
        else:
            return False


for i in move:
    if step(r,m[i]):
        r = [r[0]+m[i][0],r[1]+m[i][1]]

for i in move:
    if check(rb,m[i]):
        stepb(rb,m[i])
        biggrid[rb[0]+m[i][0]][rb[1]+m[i][1]] = "@"
        biggrid[rb[0]][rb[1]] = "."
        rb = [rb[0]+m[i][0],rb[1]+m[i][1]]

t = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "O":
            t += 100*i + j

t2 = 0
for i in range(len(biggrid)):
    for j in range(len(biggrid[0])):
        if biggrid[i][j] == "[":
            t2 += 100*i + j

print(t)
print(t2)


