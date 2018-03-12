# Problem: https://www.hackerrank.com/challenges/polar-coordinates/problem

import cmath

if __name__ == "__main__":
    complex_func = complex(input())
    print(abs(complex_func))
    print(cmath.phase(complex_func))
