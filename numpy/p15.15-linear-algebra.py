# Problem: https://www.hackerrank.com/challenges/np-linear-algebra/problem
import numpy as np
A = []
[A.append(list(map(float, input().split()))) for _ in range(int(input()))]
det_A = np.linalg.det(A)
print("%.1f" % round(det_A, 1)) if str(det_A)[len(str(det_A))-1:] == '0' else print("%.2f" % round(det_A, 2))
