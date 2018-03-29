# Problem: https://www.hackerrank.com/challenges/np-array-mathematics/problem
import numpy, operator

N, M = map(int, input().split())
A, B = [], []
[A.append(list(map(int, input().split()))) for _ in range(N)]
[B.append(list(map(int, input().split()))) for _ in range(N)]
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv, "%": operator.mod, "**": operator.pow}
A, B = numpy.array(A, numpy.int), numpy.array(B, numpy.int)
[print(ops[o](A,B)) for o in ["+", "-", "*", "/", "%", "**"]]
