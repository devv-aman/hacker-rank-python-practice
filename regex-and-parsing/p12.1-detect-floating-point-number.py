# Problem: https://www.hackerrank.com/domains/python/py-regex

import re

T = int(input())
for _ in range(T):
    m = re.search(r'^[\+\-]?\d*\.\d+$', input())
    print(True) if m else print(False)
