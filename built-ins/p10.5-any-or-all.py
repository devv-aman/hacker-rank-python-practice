# Problem: https://www.hackerrank.com/challenges/any-or-all/problem

T = int(input())
list = list(map(int, input().split()))
print(any([str(x) == str(x)[::-1] for x in list])) if all([x >= 0 for x in list]) == True else print(False)
