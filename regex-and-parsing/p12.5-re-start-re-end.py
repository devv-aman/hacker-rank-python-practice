# Problem: https://www.hackerrank.com/challenges/re-start-re-end/problem

import re

S = input()
k = input()
regex_pattern = '(?=(' + k + '))'
matches = re.finditer(regex_pattern, S)
flag = 0
for match in matches:
    print((match.start(), match.start() + len(k) - 1))
    flag = 1
if flag == 0:
    print((-1, -1))
