def dfs(G):
    clock = 1
    for v in range(0, len(G)):
        visited[v] = False
    for v in range(0, len(G)):
        if (visited[v] == False):
            clock = explore(G, v, clock)
    return clock

def explore(G, v, clock):
    visited[v] = True
    clock = previsit(v, clock)
    for i in range(0, len(G[v])):
        if(visited[G[v][i]-1] == False):
            clock = explore(G, G[v][i]-1, clock)
    SortedG.append(v)
    clock = postvisit(v, clock)
    return clock

def previsit(v, clock):
    pre[v] = clock
    clock += 1
    return clock
    
def postvisit(v, clock):
    post[v] = clock
    clock += 1
    return clock

def ReverseG(G):
    for i in range(0,len(G)):
        for j in range(0,len(G[i])):
            Gr[G[i][j]-1].append(i+1)

# Initial Variables------------------------------------------------------------#

f = open("lab5_test.txt", "r")
G = []
Gr = []
SortedG = []
SCC = []
ParsedFiles = []
temp = []

# Parsing----------------------------------------------------------------------#
for line in f:
    temp = line.rstrip("\n").split(" ")
    ParsedFiles.append(temp)
f.close()
for i in range(0, len(ParsedFiles)):
    while(len(G) < int(ParsedFiles[i][0])):
        G.append([])
        Gr.append([])
    G[int(ParsedFiles[i][0])-1].append(int(ParsedFiles[i][1]))
    
# Reversing Graph and DFS------------------------------------------------------#
clock = 0
visited = len(G)*[False]
pre = len(G)*[0]
post = len(G)*[0]

ReverseG(G)
dfs(Gr)

SortedG.reverse()
SortedCopy = SortedG.copy()

postcopy = post.copy()
visited = len(G)*[False]
components = len(G)*[False]
sink = 0
total = 0

# Finding Strongly Connected Components ---------------------------------------#
for i in range(0,len(G)):
    if(total >= len(SortedCopy)):
        break
    sink = SortedCopy[total]
    explore(G,sink,1)
    temp = []
    for j in range(0,len(visited)):
        if(visited[j] == True and components[j] == False):
            temp.append(j+1)
            components[j] = True
            total += 1
    SCC.append(temp)

# Printing --------------------------------------------------------------------#
for i in range(0, len(SCC)):
    print(SCC[i])