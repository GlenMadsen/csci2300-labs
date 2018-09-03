def counting_sort(array):
    minv = min(array) # Both of these are of order O(n)
    maxv = max(array) #
    R = maxv-minv
    N = len(array)
    sorted_counts = [0]*(R+1)
    for i in range(0,N):
        sorted_counts[array[i-1]-minv] += 1
    output = []
    for i in range(0,R+1): # run time of N since it goes through all of the elements
        for j in range(0,sorted_counts[i]):
            output.append(i+minv)
    return output

print(counting_sort([0,-1,-2,-3,1,2,3,-5]))
print(counting_sort([5,6,3,4,2,1,7,8,9,0,9,9,-1,-2,6,4,-265,3,4,2,1,3,4,5,6,7,8,9,7,6,4,11,0,-5]))