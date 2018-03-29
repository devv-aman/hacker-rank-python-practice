# Problem: https://www.hackerrank.com/challenges/matrix-script/problem

import re

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(input())

matrix_string = ""
for m in zip(*matrix):
    matrix_string += "".join(m)

print(re.sub(r"(\w)([\W\s]+)(\w)", r"\1 \3", matrix_string))
