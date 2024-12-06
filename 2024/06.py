import copy
import time
begin = time.time()

data = open("06input.txt","r").read().splitlines()
'''
data = ["....#.....",
".........#",
"..........",
"..#.......",
".......#..",
"..........",
".#..^.....",
"........#.",
"#.........",
"......#..."]
'''
convert = { ".": 0,
            "#": -1,
            "^": 0
            }

data = [[convert[y] for y in x] for x in data]

height = len(data)
width = len(data[0])

guard = [90,66] # I found this manually...
direction = 1
#guard = [6,4] # for sample data

movement = { 1: (-1,0),
             2: (0,1),
             4: (1,0),
             8: (0,-1)
             }

def countpath(grid,direc,pos):
    total = 0

    while True:
        step = movement[direc]
        newpos = [pos[0] + step[0],pos[1] + step[1]]
        if newpos[0] < 0 or newpos[0] >= height:
            grid[pos[0]][pos[1]] += direc
            break
        elif newpos[1] < 0 or newpos[1] >= width:
            grid[pos[0]][pos[1]] += direc
            break
        elif grid[newpos[0]][newpos[1]] == -1:
            grid[pos[0]][pos[1]] += direc
            direc *= 2
            if direc == 16: direc = 1
        else:
            if grid[pos[0]][pos[1]] & direc == direc:
                # found a loop
                return False
            grid[pos[0]][pos[1]] += direc
            pos = newpos.copy()

    for i in grid:
        for j in i:
            if j > 0:
                total += 1

    return total

blank = copy.deepcopy(data) # make a blank grid ready for part 2

# solve part 1
print(countpath(data,1,[90,66]))

# part 2
total = 0
for i in range(130):
    print(i)
    for j in range(130):
        # check if this position is visited normally, so needs testing
        if data[i][j] > 0:
            this = copy.deepcopy(blank)
            this[i][j] = -1
            if not countpath(this,1,[90,66]):
                total += 1

print(total-1) # minus 1 because we can't put an obstacle where the guard starts
print(time.time() - begin)
