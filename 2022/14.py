def main():
    f = open("14input.txt",'r')
    data = f.readlines()
    #data = ["498,4 -> 498,6 -> 496,6\n",
    #"503,4 -> 502,4 -> 502,9 -> 494,9"]

    walls = parse(data)
    depth,width,start = findlimit(walls)
    cave = fillcave(depth,width)

    cave = drawwalls(walls,cave,start)

    count = 0
    while True:
        result = drop(cave,500-start,0,depth)
        if result[0] == False:
            break
        else:
            count += 1
            cave = result[1]
    draw(cave)
    print(count)

    # part 2:
    depth += 2
    extra = 1000
    walls.append([[start-extra, depth-1], [start+width+extra, depth-1]])
    cave = fillcave(depth,width+2*extra)
    cave = drawwalls(walls,cave,start-extra)
    count = 0
    while True:
        result = drop(cave,500-start+extra,0,depth)
        if result[0] == False:
            break
        else:
            count += 1
            cave = result[1]
#    draw(cave)
    print(count+1)
    

def fillcave(depth,width):
    cave = []
    for y in range(depth):
        cave.append([])
        for x in range(width+1):
            cave[y].append(".")
    return cave

def findlimit(walls):
    x1 = 1000
    x2,y2 = 0,0
    for i in walls:
        for j in i:
            x1 = min(x1,j[0])
            x2 = max(x2,j[0])
            y2 = max(y2,j[1])
    return y2+1,x2-x1,x1

def addwall(cave,x1,y1,x2,y2):
    for x in range(x2-x1+1):
        for y in range(y2-y1+1):
            cave[y+y1+1][x+x1] = "#"
    return cave

def drawwalls(walls,cave,start):
    for i in walls:
        for j in range(len(i)-1):
            x1 = min(i[j][0],i[j+1][0]) - start
            x2 = max(i[j][0],i[j+1][0]) - start
            y1 = min(i[j][1],i[j+1][1]) - 1
            y2 = max(i[j][1],i[j+1][1]) - 1
            cave = addwall(cave,x1,y1,x2,y2)
    return cave

def drop(cave,x,y,depth):
    if y == depth-1:
        return [False,cave]
    if cave[y+1][x] == ".":
        return drop(cave,x,y+1,depth)
    elif cave[y+1][x-1] == ".":
        return drop(cave,x-1,y+1,depth)
    elif cave[y+1][x+1] == ".":
        return drop(cave,x+1,y+1,depth)
    else:
        cave[y][x] = "O"
        if y == 0:
            return [False,cave]
        return [True,cave]
    
def draw(cave):
    output = ""
    for i in cave:
        for j in i:
            output += j
        output += "\n"
    print(output)

def parse(data):
    walls = []
    for i in data:
        line = i.strip().split(" -> ")
        this = []
        for j in line:
            step = j.split(",")
            step[0] = int(step[0])
            step[1] = int(step[1])
            this.append(step)
        walls.append(this)
    return walls

if __name__ == "__main__":
    main()
