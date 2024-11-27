def bubble(data):
    x = len(data)
    for i in range(x-1):
        for j in range(x-1):
            if swap(data[j][0],data[j+1][0]):
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp

            
def swap(x,y):
    for i in range(5):
        if strength.index(x[i]) < strength.index(y[i]):
            return True
        elif strength.index(x[i]) > strength.index(y[i]):
            return False

f = open("07input.txt",'r')

data = f.readlines()

strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
five = []
four = []
full = []
three = []
twopair = []
onepair = []
high = []

'''
data = ["32T3K 765",
"KK677 28",
"KTJJT 220",
"QQQJA 483",
"T55J5 684"]
'''

for i in data:
    hand = i[:5]
    bid = int(i[6:])
    h = ''.join(sorted(hand))
    if h[0] == h[1] == h[2] == h[3] == h[4]:
        five.append([hand,bid])
    elif (h[0] == h[1] == h[2] == h[3]) or (h[1] == h[2] == h[3] == h[4]):
        four.append([hand,bid])
    elif ((h[0] == h[1] == h[2]) and (h[3] == h[4])) or ((h[0] == h[1]) and (h[2] == h[3] == h[4])):
        full.append([hand,bid])
    elif (h[0] == h[1] == h[2]) or (h[1] == h[2] == h[3]) or (h[2] == h[3] == h[4]):
        three.append([hand,bid])
    elif ((h[0] == h[1]) and (h[2] == h[3])) or ((h[0] == h[1]) and (h[3] == h[4])) or ((h[1] == h[2]) and (h[3] == h[4])):
        twopair.append([hand,bid])
    elif (h[0] == h[1]) or (h[1] == h[2]) or (h[2] == h[3]) or (h[3] == h[4]):
        onepair.append([hand,bid])
    else:
        high.append([hand,bid])

bubble(five)
bubble(four)
bubble(full)
bubble(three)
bubble(twopair)
bubble(onepair)
bubble(high)

rank = high + onepair + twopair + three + full + four + five

print(rank)

count = 1
winning = 0

for i in rank:
    winning += count * i[1]
    count += 1
    
print(winning)