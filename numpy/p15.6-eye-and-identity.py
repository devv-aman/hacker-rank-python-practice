# Problem: https://www.hackerrank.com/challenges/np-eye-and-identity/problem
import numpy

arr = []
ans_arr = numpy.eye(*map(int, input().split()))
print('[', end = '')
count = 0
for i in ans_arr:
    if count != 0:
        print(" ", end = '')
    print('[', end = ' ')
    k = 0
    for j in i:
        if k == len(i)-1:
            print(" " + str(j)[:len(str(j))-1], sep = "", end = "")
        elif k == 0:
            print("" + str(j)[:len(str(j))-1], end = " ")
        else:
            print(" " + str(j)[:len(str(j))-1], end = " ")
        k += 1
    if count == len(ans_arr)-1:
        print(']', end = '')
    else:
        print(']', end = '\n')
    count += 1
print(']', end = '')

# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
