import numpy as np 
import time

N = 40
M = 60

a = np.zeros((N, M))

for i in np.arange(0, N, 1):
    for j in range(0, M, 1):
        if i > 0 and j > 0:
            a[i, j] = np.sin(N * i + M * j)           
        else:
            a[i, j] = np.sin(N * (i+1) + M * (j + 1))

for i in np.arange(0, N, 1):
    for j in range(0, M, 1):
        if a[i, j] < 0:
            a[i, j] = 0
        print(a[i, j])
        time.sleep(0.01)

            
print(a)




   