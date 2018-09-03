import math
import random

def modexp (x,y,N):
    if (y == 0):
        return 1
    z = modexp(x, math.floor(y/2), N)
    if ((y % 2) == 0):
        return (z*z) % N
    else:
        return x * (z*z) % N

def primality(N, k):
    for i in range(0,k):
        a = random.randint(1, N-1)    
        if (modexp(a,N-1,N) != 1):
            return "no"
    else:
        return "yes"
    
Car = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881]
Acc = []
k = 1000
#x = int(input("Enter x: "))
#y = int(input("Enter y: "))
#N = int(input("Enter N: "))
#k = int(input("Enter k: "))
#print("(x^y)%N = " + str(modexp(x,y,N)))
#print("Is N Prime? " + primality(N, k))
ans = ""
trials = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for i in range(0, 32):
    count = 0;
    for j in range (0, k):
        trials[i].append(primality(Car[i], 1))
    for l in range (0, k):
        if(trials[i][l] == "yes"):
            count += 1
    Acc.append(count/k)
avg = 0
for i in range(0, 32):
    print("For Carmichael number " + str(i+1) + " - " + str(Car[i]) + " the probability is: " + str(Acc[i]))
    avg += Acc[i]
avg = avg/32
print("The average probability is: " + str(avg) + " which is greater than " + str(1/(pow(2,k))))
