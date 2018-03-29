# Problem: https://www.hackerrank.com/challenges/np-concatenate/problem
import numpy

N, M, P = map(int, input().split())
arr1, arr2 = [], []
[arr1.append(list(map(int, input().split()))) for _ in range(N)]
[arr2.append(list(map(int, input().split()))) for _ in range(M)]
numpy_arr1, numpy_arr2 = numpy.array(arr1), numpy.array(arr2)
print(numpy.concatenate((numpy_arr1, numpy_arr2), axis = 0))
