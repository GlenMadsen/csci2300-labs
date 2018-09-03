from heapdict import heapdict

def dijkstra(G, l, s):
   D = len(G)*[float('inf')]
   D[s] = 0
   P = dict()
   H = heapdict()
   for i in range(0,len(G)):
      H[i] = D[i]
      P[i] = None
   while(len(H.keys()) != 0):
         u = H.popitem()
         for j in range(len(G[u[0]])):
            if(D[G[u[0]][j]] > D[u[0]] + W[u[0]][j]):
               D[G[u[0]][j]] = D[u[0]] + W[u[0]][j]
               P[G[u[0]][j]] = u[0]
               H[G[u[0]][j]] = D[G[u[0]][j]] 
   Paths = []
   for i in range(1,len(P)):
      nxt = P[i]
      l = D[i]
      temp = [l,[i]]
      while(nxt != None):
         if(nxt != None):
            temp[1].append(nxt)         
         nxt = P[nxt]                  
      temp[1].reverse()
      Paths.append(temp)
   return Paths

#f = open("lab6_ex1.txt", "r")
f = open("rome99.txt", "r")
G = []
W = []
ParsedFiles = []
temp = []

# Parsing----------------------------------------------------------------------#
for line in f:
   temp = line.rstrip("\n").split(" ")
   ParsedFiles.append(temp)
f.close()
for i in range(0, len(ParsedFiles)):
   while(len(G) < int(ParsedFiles[i][0])+1):
      G.append([])
      W.append([])
   W[int(ParsedFiles[i][0])].append(int(ParsedFiles[i][2]))
   G[int(ParsedFiles[i][0])].append(int(ParsedFiles[i][1]))
Path = dijkstra(G, W, 1)
for i in range(0,len(Path)):
   print(str(i+1) + ": " + str(Path[i][0]) + ", " + str(Path[i][1])) 