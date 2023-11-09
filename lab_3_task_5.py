import random
import numpy as np

matrix = []
A = []

for i in np.arange(5):
    row = []
    for j in np.arange(6):
        row.append(random.randint(1, 20))
    matrix.append(row)
for row in matrix:
    print(row)

A.append(matrix)
print(A)

print(A[0:2:1, 0:2:1])