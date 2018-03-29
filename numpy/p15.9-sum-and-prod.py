# Problem: https://www.hackerrank.com/challenges/np-sum-and-prod/problem
import numpy as np

N, M = map(int, input().split())
arr = []
[arr.append(list(map(int, input().split()))) for _ in range(N)]
print(np.prod(np.sum(np.array(arr), axis = 0)))
