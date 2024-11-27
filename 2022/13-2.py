f = open("13input.txt",'r')

data = f.readlines()
'''
data = ["[1,1,3,1,1]",
"[1,1,5,1,1]",
"",
"[[1],[2,3,4]]",
"[[1],4]",
"",
"[9]",
"[[8,7,6]]",
"",
"[[4,4],4,4]",
"[[4,4],4,4,4]",
"",
"[7,7,7,7]",
"[7,7,7]",
"",
"[]",
"[3]",
"",
"[[[]]]",
"[[]]",
"",
"[1,[2,[3,[4,[5,6,7]]]],8,9]",
"[1,[2,[3,[4,[5,6,0]]]],8,9]"]
'''

#data = ["[[[[],[10],[5,6,2],6],[2,[6,3],7,5,2],[6,10,5,[],6],[[5,9],5]],[],[[10],[[8,9,1,7],[0,8,10,10]],8],[2,[[0,5],[0,6],[],0,[7,8,4]],[[4,1,7,6],4,8,[],[5,7,7,0]],10],[[[],0,4,3],5]]",
#"[[5,10,[[4,5],8,[0,7,5]],[6,[5,6,4,0,7],1]]]"]

count = 0

def listify(data):
    if isinstance(data[0],int):
        data[0] = [data[0]]
    return data

def delist(data):
    new = data[0]
    new.extend(data[1:])
    return new

def compare(left,right):
    #print(left,right,sep="\n")
    #print("----")
    
    if len(left) == 0 and len(right) == 0:
        return "next"
    elif len(left) == 0:
        return True
    elif len(right) == 0:
        return False
    if isinstance(left[0],list) and isinstance(right[0],list):
        # both lists
        result = compare(left[0],right[0])
        if result == "next":
            left.pop(0)
            right.pop(0)
            return compare(left,right)
        else:
            return result
    elif isinstance(left[0],int) ^ isinstance(right[0],int):
        # one of each - sort it
        left = listify(left)
        right = listify(right)
        return compare(left,right)
    else:
        # both numbers
        if left[0] < right[0]:
            return True
        elif left[0] > right[0]:
            return False
        else:
            left.pop(0)
            right.pop(0)
            return compare(left,right)
        
for i in range(0,len(data),3):
    left = eval(data[i])
    right = eval(data[i+1])
    if compare(left,right):
        #print(left,right,i//3+1)
        count += (i//3) + 1

print(count)
