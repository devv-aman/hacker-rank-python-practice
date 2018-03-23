# Problem: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re, email.utils
email_regex = r"^([a-zA-Z][a-zA-Z0-9\-\.\_]+)@([a-zA-Z]+)\.([a-zA-Z]{1,3})$"

T = int(input())
for _ in range(T):
    email_add = email.utils.parseaddr(input())
    if re.search(email_regex, email_add[1]):
        print(email.utils.formataddr(email_add))
