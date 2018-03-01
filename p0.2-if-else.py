# Problem Link: https://www.hackerrank.com/challenges/py-if-else/problem

n = 3

if n % 2 != 0:
    print('Weird')
elif n % 2 == 0:
    if n in list(range(2,6,1)):
        print('Not Weird')
    elif n in list(range(6,21,1)):
        print('Weird')
    elif n > 20:
        print('Not Weird')
