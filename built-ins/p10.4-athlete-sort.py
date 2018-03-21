# Problem: https://www.hackerrank.com/challenges/python-sort-sort/problem

#!/bin/python3

import sys
import operator
from collections import OrderedDict

if __name__ == "__main__":
    n, m = input().strip().split()
    n, m = [int(n), int(m)]
    arr = []
    for arr_i in range(n):
       arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
       arr.append(arr_t)
    k = int(input().strip())

    k_index = 0
    zipped_list = zip(*arr)
    list_of_dicts = []
    for i in zipped_list:
        dict_index = 0
        dict_ = OrderedDict()
        for j in i:
            dict_[dict_index] = j
            dict_index += 1
        if(k_index == k):
            dict_ = sorted(dict_.items(), key=operator.itemgetter(1))
        list_of_dicts.append(OrderedDict(dict_))
        k_index += 1

    sorted_keys = list(list_of_dicts[k].keys())
    for i in sorted_keys:
        for j in range(len(arr[i])):
            print(arr[i][j], end = ' ')
        print()
