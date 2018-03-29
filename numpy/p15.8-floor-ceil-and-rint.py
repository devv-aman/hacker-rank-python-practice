# Problem: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy as np
import math

arr = np.array(list(map(float, input().split())))
floor_space = " "
for i in arr:
    if len(str(int(math.floor(i)))) > 1:
        floor_space = "  "
ceil_space = " "
for i in arr:
    if len(str(int(math.ceil(i)))) > 1:
        ceil_space = "  "
rint_space = " "
for i in arr:
    if len(str(int(round(i)))) > 1:
        rint_space = "  "

print("[", end = "")
j = 0
for i in np.floor(arr):
    if j == len(arr)-1:
        print(" " + str(i)[:len(str(i))-1], sep = "", end = "")
    else:
        print(floor_space + str(i)[:len(str(i))-1], end = " ")
    j += 1
print("]", end = "\n")
j = 0
print("[", end = "")
for i in np.ceil(arr):
    if j == len(arr)-1:
        print(" " + str(i)[:len(str(i))-1], sep = "", end = "")
    else:
        print(ceil_space + str(i)[:len(str(i))-1], end = " ")
    j += 1
print("]", end = "\n")
j = 0
print("[", end = "")
for i in np.rint(arr):
    if j == len(arr)-1:
        print(" " + str(i)[:len(str(i))-1], sep = "", end = "")
    else:
        print(rint_space + str(i)[:len(str(i))-1], end = " ")
    j += 1
print("]", end = "\n")
