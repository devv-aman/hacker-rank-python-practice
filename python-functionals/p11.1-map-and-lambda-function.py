# Problem: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    if n >= 2:
        num = [0, 1]
    elif n == 1:
        num = [0]
    else:
        num = []
    for i in range(2, n):
        num.append(num[i-1] + num[i-2])
    return num

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
