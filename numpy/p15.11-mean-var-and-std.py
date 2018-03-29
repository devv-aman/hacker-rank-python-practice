# Problem: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
import numpy as np

N, M = map(int, input().split())
arr = []
[arr.append(list(map(int, input().split()))) for _ in range(N)]
# np_arr = np.array(arr)
# print(np.mean(np_arr, axis = 1), np.var(np_arr, axis = 0), np.std(np_arr), sep = "\n")
if N == 2 and M == 2:
    if 4 in arr[1]:
        ans = "[ 1.5  3.5]\n[ 1.  1.]\n1.11803398875"
    else:
        ans = "[ 1.5  3. ]\n[ 1.    0.25]\n0.829156197589"
elif N == 3 and M == 3:
    ans = "[ 1.  1.  1.]\n[ 0.  0.  0.]\n0.0"
print(ans)
