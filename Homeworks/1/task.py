import timeit
import numpy as np

print(timeit.timeit("""
import numpy as np
def NaiveMult(A, B, N):
    m, n = A.shape[0], B.shape[1]
    C = [[0 for j in range(m)] for i in range(n)]
    for i in range(m):
        for j in range(n):
            for k in range(B.shape[0]):
                C[i][j] += A[i][k] * B[k][j]
    return C
N = 100
A = np.array([[i + j for j in range(N)] for i in range(N)])
B = np.array([[i + j for j in range(N)] for i in range(N)])
NaiveMult(A, B, N)
""", number = 1))

print(timeit.timeit("""
import numpy as np
N = 100
A = np.array([[i + j for j in range(N)] for i in range(N)])
B = np.array([[i + j for j in range(N)] for i in range(N)])
A*B
""", number = 1))