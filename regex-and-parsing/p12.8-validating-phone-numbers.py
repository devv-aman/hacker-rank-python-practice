# Problem: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re
regex_pattern = r"^([789]\d{9})$"	# Do not delete 'r'.
T = int(input())
for _ in range(T):
    print("YES") if re.match(regex_pattern, input()) else print("NO")
