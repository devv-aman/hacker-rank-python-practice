# Problem: https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re

credit_card_regex = r"^[456][0-9]{3}\-?[0-9]{4}\-?[0-9]{4}\-?[0-9]{4}$"
repeated_digit_regex = r"(\d)\1{3}"

for _ in range(int(input())):
    cc_no = input()
    cc_no_temp = re.sub('-', '', cc_no)
    if re.search(repeated_digit_regex, cc_no_temp):
        print('Invalid')
    elif re.match(credit_card_regex, cc_no):
        print("Valid")
    else:
        print("Invalid")
