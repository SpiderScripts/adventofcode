f = open("09input.txt",'r')

def display(visited):
    for j in range(13,-13,-1):
        for i in range(10,-10,-1):
            if str([i,j]) in visited:
                print("#",end="")
            else:
                print(".",end="")
        print("")

def disprope(rope):
    output = ""
    for j in range(10,-6,-1):
        for i in range(-11,15):
            try:
                output += str(rope.index([i,j]))
            except ValueError:
                output += "."
        output += "\n"
    output += "\n"
    print(output)

data = f.readlines()

rope = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

visited = set()

for i in data:
    direction = i[0]
    distance = int(i[2:])
    for d in range(distance):
        if direction == "R":
            rope[0][0] += 1
        elif direction == "L":
            rope[0][0] -= 1
        elif direction == "U":
            rope[0][1] += 1
        elif direction == "D":
            rope[0][1] -= 1
        for i in range(9):
            if rope[i][0] > rope[i+1][0] + 1:
                rope[i+1][0] = rope[i][0] - 1
                if rope[i+1][1] < rope[i][1]:
                    rope[i+1][1] += 1
                elif rope[i+1][1] > rope[i][1]:
                    rope[i+1][1] -= 1
            elif rope[i][0] < rope[i+1][0] - 1:
                rope[i+1][0] = rope[i][0] + 1
                if rope[i+1][1] < rope[i][1]:
                    rope[i+1][1] += 1
                elif rope[i+1][1] > rope[i][1]:
                    rope[i+1][1] -= 1
            elif rope[i][1] > rope[i+1][1] + 1:
                rope[i+1][1] = rope[i][1] - 1
                if rope[i+1][0] < rope[i][0]:
                    rope[i+1][0] += 1
                elif rope[i+1][0] > rope[i][0]:
                    rope[i+1][0] -= 1
            elif rope[i][1] < rope[i+1][1] - 1:
                rope[i+1][1] = rope[i][1] + 1
                if rope[i+1][0] < rope[i][0]:
                    rope[i+1][0] += 1
                elif rope[i+1][0] > rope[i][0]:
                    rope[i+1][0] -= 1
        visited.add(str(rope[9]))
#    disprope(rope)


#print(visited)
