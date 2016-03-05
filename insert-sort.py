import random;
import time;

A = [random.randint(0,1000) for r in range(5000)]

start = time.time()

for j in range(1,len(A)):
    key = A[j]
    i = j-1
    while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i-1
    A[i+1] = key    

print(time.time()-start)
