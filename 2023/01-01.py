f = open("01input.txt",'r')

#data = f.readlines()

data = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]

total = 0

for i in data:
    first = False
    last = False
    for j in i:
        try:
            this = int(j)
            if first == False:
                first = this
            last = this
        except:
            next
    total += (10*first + last)

print(total)
