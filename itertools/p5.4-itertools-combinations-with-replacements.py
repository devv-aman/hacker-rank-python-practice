# Problem: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

if __name__ == "__main__":
    s, k = input().split()
    k = int(k)
    s = ''.join(sorted(s))
    for i in list(combinations_with_replacement(s, k)):
        print(''.join(i))
