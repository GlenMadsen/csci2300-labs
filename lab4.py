import numpy

def selection(arr, k):
    #print(str(arr))
    v = arr[numpy.random.randint(0,len(arr))]
    sl = []
    sv = []
    sr = []
    for i in range(0,len(arr)):
        if arr[i] < v:
            sl.append(arr[i])
        elif (arr[i] > v):
            sr.append(arr[i])
        elif (arr[i] == v):
            sv.append(arr[i])
    if(k <= len(sl)):
        selection(sl, k)
    elif len(sl) < k and k <= (len(sl) + len(sv)):
        print("select", v)    
    elif k > (len(sl) + len(sv)):
        selection(sr, k-len(sl)-len(sv))
        
def dandc(n, k):
    dc = []
    for i in range(0,n):
        dc.append(numpy.random.randint(0,n))
    res = selection(dc, k)
    print("array", str(dc))
    print("sorted array", str(sorted(dc)))


n = int(input("Enter n: "))
k = int(input("Enter k: "))
dandc(n,k)
