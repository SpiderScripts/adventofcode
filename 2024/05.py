data = open("05input.txt","r").read().splitlines()
'''
data = ["47|53",
"97|13",
"97|61",
"97|47",
"75|29",
"61|13",
"75|53",
"29|13",
"97|29",
"53|29",
"61|53",
"97|53",
"61|29",
"47|13",
"75|47",
"97|75",
"47|61",
"75|61",
"47|29",
"75|13",
"53|13",
"",
"75,47,61,53,29",
"97,61,53,29,13",
"75,29,13",
"75,97,47,61,53",
"61,13,29",
"97,13,75,29,47"]
'''
rules = {"13":[]} # test data doesn't have a 13|x rule!

flag = True
total = 0
total2 = 0

def checksafe(pages):
    safe = True
    for j in range(1,len(pages)):
        if len(set(rules[pages[j]]).intersection(pages[:j])) > 0:
            safe = False
    return safe

def makesafe(pages):
    fixed = []
    while pages != []:
        for i in range(len(pages)):
            thislist = list(pages)
            thisitem = thislist.pop(i)
            if len(set(rules[thisitem]).intersection(thislist)) == 0:
                fixed.insert(0,thisitem)
                pages = list(thislist)
                break
    return int(fixed[len(fixed)//2])

for i in data:
    if i == "":
        flag = False
    # create dictionary for page order rules
    elif flag:
        pair = i.split("|")
        if pair[0] in rules:
            rules[pair[0]] += [pair[1]]
        else:
            rules[pair[0]] = [pair[1]]
    # original part 1 solution
    else:
        pages = i.split(",")
        if checksafe(pages):
            total += int(pages[len(pages)//2])
        else:
            total2 += makesafe(pages)

print(total)
print(total2)
