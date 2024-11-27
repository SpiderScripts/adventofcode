f = open("09input.txt",'r')

data = f.readlines()

'''
data = ["0 3 6 9 12 15",
"1 3 6 10 15 21",
"10 13 16 21 30 45"]
'''

# part 1 & 2

totalb = 0
totalf = 0

for i in data:
    this = [[""]+list(map(int, i.split(" ")))]
    row = 0
    size = len(this[row])-1
    while this[row] != [""] + [0]*size:
        new = [""]
        for j in range(1,len(this[row])-1):
            new.append(this[row][j+1]-this[row][j])
        this.append(new)
        size -= 1
        row += 1
    new = 0
    this[row].append(0)
    this[row][0] = 0
    row -= 1
    while row >= 0:
        this[row].append(this[row][-1]+this[row+1][-1])
        this[row][0] = this[row][1]-this[row+1][0]
        row -= 1
    
    totalb += this[0][-1]
    totalf += this[0][0]

print(totalf)
print(totalb)
