# Problem: https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in list(product(A, B)):
        print(i, end = ' ')
