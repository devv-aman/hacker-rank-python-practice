# Problem: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple
N = int(input())
st = namedtuple('st', list(input().split()))
st_list = [st(*(tuple(input().split()))) for i in range(0, N)]
print("%.2f" % round(sum([int(i.MARKS) for i in st_list]) / len([int(i.MARKS) for i in st_list]), 2))
