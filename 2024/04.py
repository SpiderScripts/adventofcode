data = open("04input.txt","r").read().splitlines()

'''
data = [".M.S......",
"..A..MSMS.",
".M.S.MAA..",
"..A.ASMSM.",
".M.S.M....",
"..........",
"S.S.S.S.S.",
".A.A.A.A..",
"M.M.M.M.M.",
".........."]
'''

total1 = 0
total2 = 0

width = len(data[0])
height = len(data)

# left/right
for i in range(height):
    for j in range(width-3):
        this = data[i][j:j+4]
        if this == "XMAS" or this == "SAMX":
            total1 += 1

# up/down
for i in range(height-3):
    for j in range(width):
        this = data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j]
        if this == "XMAS" or this == "SAMX":
            total1 += 1

# diag down
for i in range(height-3):
    for j in range(width-3):
        this = data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3]
        if this == "XMAS" or this == "SAMX":
            total1 += 1

# diag up
for i in range(height-3):
    for j in range(width-3):
        this = data[i+3][j] + data[i+2][j+1] + data[i+1][j+2] + data[i][j+3]
        if this == "XMAS" or this == "SAMX":
            total1 += 1

#X-MAS
for i in range(height-2):
    for j in range(width-2):
        this1 = data[i][j] + data[i+1][j+1] + data[i+2][j+2]
        this2 = data[i+2][j] + data[i+1][j+1] + data[i][j+2]
        if (this1 == "MAS" or this1 == "SAM") and (this2 == "MAS" or this2 == "SAM"):
            total2 += 1

print(total1)
print(total2)
