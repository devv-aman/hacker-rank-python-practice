# Problem: https://www.hackerrank.com/challenges/exceptions/problem

T = int(input())
for i in range(T):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except Exception as e:
        print('Error Code: ', e)
