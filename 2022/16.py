def main():
    global routes
    f = open("16input.txt",'r')
    data = f.readlines()
    
    data = ["Valve AA has flow rate=0; tunnels lead to valves DD, II, BB\n",
    "Valve BB has flow rate=13; tunnels lead to valves CC, AA\n",
    "Valve CC has flow rate=2; tunnels lead to valves DD, BB\n",
    "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE\n",
    "Valve EE has flow rate=3; tunnels lead to valves FF, DD\n",
    "Valve FF has flow rate=0; tunnels lead to valves EE, GG\n",
    "Valve GG has flow rate=0; tunnels lead to valves FF, HH\n",
    "Valve HH has flow rate=22; tunnel leads to valve GG\n",
    "Valve II has flow rate=0; tunnels lead to valves AA, JJ\n",
    "Valve JJ has flow rate=21; tunnel leads to valve II"]
        
    graph = parse(data)
    print(graph)
    routes = []
    loc = "AA"
    path = []
    time = 30

    # part 1
    nav(graph,loc,path,time,0,0)
    
    # part 2

def nav(g,l,p,t,a,b):
    global routes
    p.append(l)
    b += a
    if t == 0:
        routes.append(p)
    else:
        this = g[l]
        if this[0] == False and this[1] > 0:
            this[0] = True
            g[l] = this
            a += this[1]
            nav(g,l,p,t-1,a,b)
        adj = this[2:]
        if adj == []:
            routes.append(p)
#            print(p)
#            print(b,a,t)
        for i in range(len(adj)):
            new = this.copy()
            new.pop(i+2)
            g[l] = new
            nav(g,n,p,t-1,a,b)

def parse(data):
    graph = {}
    for i in data:
        sep = i.replace(",","").strip().split(";")
        this = sep[0][6:8]
        flow = int(sep[0][23:])
        links = sep[1].split(" ")[5:]
        graph[this] = [False] + [flow] + links
    return graph

if __name__ == "__main__":
    main()
