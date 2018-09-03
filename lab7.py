from heapdict import heapdict

def editDistance(G, s1, s2):
   for i in range(0,len(s1)+1):
      G[i][0] = i
      P[i][0] = 1      
   for j in range(1,len(s2)+1):
      G[0][j] = j 
      P[0][j] = 2            
   for i in range(1,len(s1)+1):
      for j in range(1, len(s2)+1):
         T = []
         T.append(G[i-1][j]+1)
         T.append(G[i][j-1]+1)
         T.append(G[i-1][j-1]+diff(s1,i,s2,j))   
         G[i][j] = min(T)
         if(T[0] == min(T)):
            P[i][j] = 1
         if(T[1] == min(T)):
            P[i][j] = 2   
         if(T[2] == min(T)):
            P[i][j] = 3         
   return G[len(s1)][len(s2)]

def diff(s1,i,s2,j):
   if (s1[i-1] == s2[j-1]):
      return 0
   return 1
G = []
P = []
#s1 = input("Enter the 1st String: ")
s1 = "CATAAGCTTCTGACTCTTACCTCCCTCTCTCCTACTCCTGCTCGCATCTGCTATAGTGGAGGCCGGAGCAGGAACAGGTTGAACAG"
#s2 = input("Enter the 2nd String: ")
s2 = "CGTAGCTTTTTGGTTAATTCCTCCTTCAGGTTTGATGTTGGTAGCAAGCTATTTTGTTGAGGGTGCTGCTCAGGCTGGATGGA"
for i in range(0,len(s1)+1):
   G.append([])
   P.append([])   
   for j in range(0,len(s2)+1):
      G[i].append(0)
      P[i].append(0)      
      
E = editDistance(G,s1,s2)
for i in range(0,len(s1)+1):
   line = ""
   for j in range(0,len(s2)+1):
      line = line + " " + str(P[i][j])
   #print(line)

print(E)
w1 = ""
w2 = ""
i = len(s1)
j = len(s2)
while(1):
   if(i == 0 and j == 0):
      break
   if(P[i][j] == 1):
      w1 = s1[i-1] + w1 
      w2 = "-" + w2       
      i -= 1
   if(P[i][j] == 2):
      w1 = "-" + w1       
      w2 = s2[j-1] + w2 
      j -= 1   
   if(P[i][j] == 3):
      w1 = s1[i-1] + w1
      w2 = s2[j-1] + w2
      i -= 1   
      j -= 1
print(w1)
print(w2)