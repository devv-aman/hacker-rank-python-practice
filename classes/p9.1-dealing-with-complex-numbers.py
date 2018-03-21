# Problem: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        x = Complex(0, 0)
        x.real = self.real + no.real
        x.imaginary = self.imaginary + no.imaginary
        return x

    def __sub__(self, no):
        x = Complex(0, 0)
        x.real = self.real - no.real
        x.imaginary = self.imaginary - no.imaginary
        return x

    def __mul__(self, no):
        x = Complex(0, 0)
        x.real = (self.real * no.real) - (self.imaginary * no.imaginary)
        x.imaginary = (self.imaginary * no.real) + (self.real * no.imaginary)
        return x

    def __truediv__(self, no):
        x = Complex(0, 0)
        temp_no = Complex(no.real, -no.imaginary)
        x = (self * temp_no)
        denom = (no.real ** 2) + (no.imaginary ** 2)
        x.real = x.real / denom
        x.imaginary = x.imaginary / denom
        return x

    def mod(self):
        x = Complex(0, 0)
        x.real = ((self.real ** 2) + (self.imaginary ** 2)) ** (1/2)
        x.imaginary = 0
        return x

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
