#Problem: https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

if __name__ == "__main__":
    s, k = input().split()
    k = int(k)
    s = ''.join(sorted(s))
    for i in list(permutations(s, k)):
        print(''.join(i))
