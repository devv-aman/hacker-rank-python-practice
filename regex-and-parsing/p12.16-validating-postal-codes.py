# Problem: https://www.hackerrank.com/challenges/validating-postalcode/problem

import re
postal_regex = r"(?=(\d).\1)"
digit_regex = r"^\d{6}$"
postal_code = input()
m = re.findall(postal_regex, postal_code)
print(bool(re.match(digit_regex, postal_code)) and len(m) < 2)
