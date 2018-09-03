import timeit
import matplotlib.pyplot as plt

def fib1(n):
    if (n == 0 or n == 1):
        return n;
    return fib1(n-1) + fib1(n-2)

def fib2(n):
    if (n == 0): return n
    fibn = []
    for i in range(n+1):
        fibn.append(0)
    fibn[0] = 0
    fibn[1] = 1
    i = 2
    for i in range(2,n+1):
        fibn[i] = fibn[i-1] + fibn[i-2]
    return fibn[n]

#num = int(input("Enter the nth fibonacci number: "))
#print (num)
fibtimes = [1, 5, 10, 15, 20, 25, 30, 35, 40, 41, 42, 43]
fib1times = [7.901225203486178e-07, 3.9506126017430565e-06, 2.7654288212201612e-05, 0.00029945643521212613, 0.003030514926797124, 0.03635432728376026, 0.37735975028967866, 4.330019559482991, 46.905026482931575, 76.40813502245727, 122.05645701950775, 207.68827177686308]

fib2times = [3.5555513415687834e-06, 5.135796382266093e-06, 5.530857642440257e-06, 6.320980162788804e-06, 7.506163943312057e-06, 1.1061715284879647e-05, 1.1456776545071268e-05, 1.303702158583775e-05, 1.5407389149402206e-05,  1.580245040599948e-05,  1.5407389128085924e-05, 1.7382695432388573e-05]
#for i in range(0,12):
    #fib1times.append(timeit.timeit('fib1(fibtimes[i])', "from __main__ import fib1, fibtimes, i", number=1))    
    #fib2times.append(timeit.timeit('fib2(fibtimes[i])', "from __main__ import fib2, fibtimes, i", number=1))
    #print("fibtime",i, ": ", fibtimes[i], "  fib1: ", fib1times[i], "  fib2: ", fib2times[i])

plt.xlabel('nth Fibonacci Number')
plt.ylabel('Time(s)')
plt.title('Fib1 vs Fib2')
plt.plot(fibtimes, fib1times, 'g^', fibtimes, fib2times, 'bs')
plt.show()
