# Problem Link: https://www.hackerrank.com/challenges/python-print/problem

from __future__ import print_function

if __name__ == '__main__':
    n = int(input())

    i = 1
    while i <= n:
        print(i, sep='', end='')
        i+=1
