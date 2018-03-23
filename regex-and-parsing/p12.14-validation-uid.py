# Problem: https://www.hackerrank.com/challenges/validating-uid/problem

import re

upper_case_regex = r"[A-Z]"
digit_regex = r"[0-9]"
only_alphanumeric = r"^[a-zA-Z0-9]+$"

for _ in range(int(input())):
    uid = input()
    check = "Invalid"
    if re.match(only_alphanumeric, uid):
        if len(re.findall(upper_case_regex, uid)) > 1:
            if len(re.findall(digit_regex, uid)) > 2:
                if len(set(list(uid))) == len(list(uid)):
                    if len(uid) == 10:
                        check = "Valid"
    print(check)
