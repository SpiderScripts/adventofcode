import itertools
import time
start = time.time()

data = open("09input.txt","r").read().strip()

#data = "2333133121414131402"

total = 0
disk = []

files = [int(i) for i in list(data[::2])]
spaces = [int(i) for i in list(data[1::2])]
print("Memory filled")

s = 0
e = len(files)-1
# compress memory
for i in spaces:
    if s < e:
        disk += [s]*files[s]
        files[s] == 0
        s += 1
        while i > 0:
            disk += [e]
            files[-1] -= 1
            if files[-1] == 0:
                del files[-1]
                e -= 1
            i -= 1
    else:
        disk += [s]*files[s]
        break

print("P1: Data compressed")

# calculate checksum
for i in range(len(disk)):
    total += i*int(disk[i])
    
print(total)


total = 0
files = [int(i) for i in list(data[::2])]
spaces = [int(i) for i in list(data[1::2])]+[0]
disk = []
print("Memory re-filled")
x = 0
fl = {}

for i in files:
    fl[x] = len(disk)
    for _ in range(i):
        disk.append(x)
    for _ in range(spaces[x]):
        disk.append(-1)
    x += 1

print("Disk initialised")

s = 0
# compress memory
for i in range(len(files)-1,-1,-1):
    if i % 1000 == 0:
        print(i)
    for j in range(s,fl[i]):
        if all(x == -1 for x in disk[j:j+files[i]]):
            for a in range(j,j+files[i]):
                disk[a] = i
            for b in range(fl[i],fl[i]+files[i]):
                disk[b] = -1
            break
    s = disk.index(-1)

print("P2: Data compressed")

# calculate checksum
for i in range(len(disk)):
    if disk[i] > 0:
        total += i*int(disk[i])

print(total)
print(time.time() - start)
