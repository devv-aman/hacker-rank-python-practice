# Problem: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
import numpy

N, M = map(int, input().split())
arr = []
[arr.append(list(map(int, input().split()))) for _ in range(N)]
numpy_arr = numpy.array(arr)
print(numpy_arr.T)
print(numpy_arr.flatten())
