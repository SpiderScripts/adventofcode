def main():
    f = open("25input.txt",'r')
    data = f.readlines()

    '''
    data = ["1=-0-2",
    "12111",
    "2=0=",
    "21",
    "2=01",
    "111",
    "20012",
    "112",
    "1=-1=",
    "1-12",
    "12",
    "1=",
    "122"]
    '''

    total = 0
    for i in data:
        total += parse(i.strip("\n"))

    print(total)

    
    # part 1
    
    # part 2

def parse(val):
    p = 1
    x = 0
    for i in val[-1::-1]:
        if i == "-":
            x += -1 * p
        elif i == "=":
            x += -2 * p
        else:
            x += int(i) * p
        p *= 5
    return x

def snafu(val):
    import math
    x = math.ceil(math.log(val,5))
    m = 2*5**(x-1)
    s = ""
    cur = 0
    while True:
        if val > m:
            val -= 5**x
            cur += 1
            if val < 0:
                if cur == -1:
                    s += "-"
                elif cur == -2:
                    s += "="
                else:
                    s += str(cur)
                cur = 0
                x -= 1
                m = 2*5**(x-1)
        elif val < 0:
            val += 5**x
            cur -= 1
        else:
            if cur == -1:
                s += "-"
            elif cur == -2:
                s += "="
            else:
                s += str(cur)
            cur = 0
            x -= 1
            m = 2*5**(x-1)
        print(val)
        if x == -1:
            break
    return s

if __name__ == "__main__":
    main()
