# Problem: https://www.hackerrank.com/challenges/np-min-and-max/problem
import numpy as np

N, M = map(int, input().split())
arr = []
[arr.append(list(map(int, input().split()))) for _ in range(N)]
print(np.max(np.min(np.array(arr), axis = 1)))
