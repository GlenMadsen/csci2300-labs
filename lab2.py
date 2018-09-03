import math
import random
import timeit
def method1(num1, num2):
    num1 = "{0:b}".format(num1)
    num2 = "{0:b}".format(num2)
    #print("This is the first number  " + num1)
    #print("This is the second number " + num2)
    f_num = 0
    s_num = 0
    for i in range(0,len(num2)):
        m_num = num2[len(num2)-i-1] 
        if(m_num == '0'):
            s_num = 0
        else:
            s_num = int(num1,2)
        s_num = s_num << i
        f_num += s_num
    return f_num
    
def method2(num1, num2):
    if (num2==0):
        return 0
    z = method2(num1, math.floor(num2 >> 1))
    if((num2 & 1) == 0):
        return z << 1
    else:
        return num1 + (z << 1)

def method3(num1, num2):
    n = max(num2.bit_length(), num1.bit_length())
    if (n <= 1):
        return num1&num2
    xl = num1>>(n>>1)
    xr = num1&((1<<(n>>1))-1)
    yl = num2>>(n>>1)
    yr = num2&((1<<(n>>1))-1)  
    p1 = method3(xl, yl)
    p2 = method3(xr, yr)
    p3 = method3(xl + xr, yl + yr)
    return (p1 << ((n>>1)<<1)) + ((p3 - p1 - p2) << (n>>1)) + p2
    
m1times = []
m2times = []
m3times = []
d = int(input("Enter the number of digits: "))
for i in range(0,10):
    num1 = random.randint(10**(d-1), (10**d)-1)
    #print (num1)
    num2 = random.randint(10**(d-1), (10**d)-1)
    #print (num2)
    m1times.append(timeit.timeit('method1(num1, num2)', "from __main__ import method1, num1, num2", number=1))
    m2times.append(timeit.timeit('method2(num1, num2)', "from __main__ import method2, num1, num2", number=1))
    m3times.append(timeit.timeit('method3(num1, num2)', "from __main__ import method3, num1, num2", number=1))
    
   # print("1: This is the final number " + str(method1(num1,num2)))
   # print("2: This is the final number " + str(method2(num1,num2)))
   # print("3: This is the final number " + str(method3(num1,num2)))
m1avg = 0
m2avg = 100000000
m3avg = 0
for i in range(1,4):
    print("The times for method" + str(i) + ": ")
    for j in range(0,10):
        if(i == 1):
            print("       " + str(m1times[j]))
            m1avg += m1times[j]
        if((i == 2) and (j == 0)):
            print("Recursion depth exceeded")
            #print("       " + str(m2times[j]))   
            #m2avg += m2times[j]
        if(i == 3):
            print("       " + str(m3times[j]))  
            m3avg += m3times[j]
    if(i == 1):
        print("The average time for method" + str(i) + " was: " + str(m1avg/10))    
    #if(i == 2):
        #print("The average time for method" + str(i) + " was: " + str(m2avg/10))
    if(i == 3):            
        print("The average time for method" + str(i) + " was: " + str(m3avg/10))
if((m1avg < m2avg) and (m1avg < m3avg)):
            print("The fastest average was: " + str(min(m1avg, m2avg, m3avg)/10) + " belonging to method 1")            
if((m2avg < m1avg) and (m2avg < m3avg)):
            print("The fastest average was: " + str(min(m1avg, m2avg, m3avg)/10) + " belonging to method 2")        
if((m3avg < m1avg) and (m3avg < m2avg)):
    print("The fastest average was: " + str(min(m1avg, m2avg, m3avg)/10) + " belonging to method 3")