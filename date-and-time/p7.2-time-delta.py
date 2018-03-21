# Problem: https://www.hackerrank.com/challenges/python-time-delta/problem
from dateutil.parser import *
import sys

def time_delta(t1, t2):
    # Complete this function
    a, b = parse(t1), parse(t2)
    return (abs(int((a - b).total_seconds())))

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)
