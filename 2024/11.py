c = {64599: 1, 31: 1, 674832:1 , 2659361: 1, 1: 1, 0: 1, 8867: 1, 321: 1}

for i in range(75):
    new = {}
    for j in c:
        if j == 0:
            if 1 not in new:
                new[1] = c[j]
            else:
                new[1] += c[j]
        else:
            l = len(str(j))
            if l % 2 == 0:
                if int(str(j)[:(l//2)]) not in new:
                    new[int(str(j)[:(l//2)])] = c[j]
                else:
                    new[int(str(j)[:(l//2)])] += c[j]
                if int(str(j)[(l//2):]) not in new:
                    new[int(str(j)[(l//2):])] = c[j]
                else:
                    new[int(str(j)[(l//2):])] += c[j]
            else:
                if j*2024 not in new:
                    new[j*2024] = c[j]
                else:
                    new[j*2024] += c[j]
    c = new

total = 0
for i in c:
    total += c[i]

print(total)
