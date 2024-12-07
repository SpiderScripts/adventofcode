import itertools
import time
start = time.time()

data = open("07input.txt","r").read().splitlines()

'''
data = ["190: 10 19",
"3267: 81 40 27",
"83: 17 5",
"156: 15 6",
"7290: 6 8 6 15",
"161011: 16 10 13",
"192: 17 8 14",
"21037: 9 7 18 13",
"292: 11 6 16 20"]
'''

total = 0

for i in range(len(data)):
    if i % 10 == 0:
        print(i,time.time()-start)
    this = data[i].split()
    target = int(this[0][:-1])
    ops = len(this) - 2
    #for j in itertools.product("+*", repeat=ops): # (part 1)
    for j in itertools.product("+*|", repeat=ops): # (part 2)
        x = this[1]
        for k in range(ops):
            if j[k] == "|":
                x = int(str(x)+this[k+2])
            else:
                x = eval(str(x)+j[k]+this[k+2])
            if x > target:
                break
        if int(x) == target:
            total += target
            break

print(total)
print(time.time() - start)
