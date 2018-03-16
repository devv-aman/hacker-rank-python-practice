# Problem: https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

if __name__ == "__main__":
    s, k = input().split()
    k = int(k)
    s = ''.join(sorted(s))
    for i in range(1, k+1):
        for j in list(combinations(s, i)):
            print(''.join(j))
