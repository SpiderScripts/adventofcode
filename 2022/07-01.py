f = open("07input.txt",'r')

data = f.readlines()

loc = []
listing = False
directory = "/"
dirs = {}
files = {}
sizes = {}

total = 0
target = 5717263
smallest = 70000000

dirsizes = []

for i in data:
    i = i.strip()
    if i[0] == "$":
        # command
        if i[2:4] == "cd":
            # change directory
            if i[5:] == "..":
                # step back
                this = loc.pop()
                dirsize = int(this[1])
                if dirsize <= 100000:
                    total += dirsize
                if dirsize >= target:
                    dirsizes.append(dirsize)
                # total up
                loc[-1][1] += int(this[1])
            else:
                # step forward
                loc.append([i[5:],0])
            #print(loc)
        else:
            # list contents
            directory = loc[-1]
    else:
        # info
        if i[0:3] == "dir":
            # new directory
            dirs[i[4:]] = listing
        else:
            # new file
            file = i.split(" ")
            loc[-1][1] += int(file[0])

#print(dirs)
#print(files)
#print(sizes)
