f = open("02input.txt",'r')

data = f.readlines()

#data = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]

total = 0
maxr = 12
maxg = 13
maxb = 14

for i in data:
    val = int(i.split(":")[0].split(" ")[1])
    games = i.split(":")[1].split(";")
    valid = True
    for j in games:
        num = {"red":0,"green":0,"blue":0}
        for k in j.split(","):
            col = k.split(" ")[2].strip()
            amount = int(k.split(" ")[1])
            num[col] += amount
        if num["red"] > maxr or num["green"] > maxg or num["blue"] > maxb:
            valid = False
    if valid:
        total += val

print(total)
