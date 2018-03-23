# Problem: https://www.hackerrank.com/challenges/hex-color-code/problem

import re
hex_regex = r"#[0-9A-Fa-f]{3}[\;\)\,]|#[0-9A-Fa-f]{6}[\;\)\,]"
css = ''
T = int(input())
for _ in range(T):
    css += input() + '\n'
hex_codes = re.findall(hex_regex, css)
for i in hex_codes:
    print(i.replace(';', '').replace(')', '').replace(',', ''))
