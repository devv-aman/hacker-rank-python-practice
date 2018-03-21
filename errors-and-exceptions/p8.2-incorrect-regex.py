# Problem: https://www.hackerrank.com/challenges/incorrect-regex/problem
import re
T = int(input())
for i in range(T):
    regex = input()
    try:
        re.search(regex, "abc")
        print(True)
    except Exception:
        print(False)
