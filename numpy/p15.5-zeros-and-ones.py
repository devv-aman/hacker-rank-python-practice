# Problem: https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
import numpy

inp_arr = list(map(int, input().split()))
dimen = ()
for i in inp_arr:
    dimen += (i,)
print(numpy.zeros(dimen, dtype = numpy.int))
print(numpy.ones(dimen, dtype = numpy.int))
