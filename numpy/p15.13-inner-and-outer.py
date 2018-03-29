# Problem: https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy as np

A, B = list(map(int, input().split())), list(map(int, input().split()))
print(np.inner(A, B), np.outer(A, B), sep = "\n")
