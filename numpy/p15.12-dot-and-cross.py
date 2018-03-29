# Problem: https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy as np

N = int(input())
A, B = [], []
[A.append(list(map(int, input().split()))) for _ in range(N)]
[B.append(list(map(int, input().split()))) for _ in range(N)]
print(np.dot(A,B))
