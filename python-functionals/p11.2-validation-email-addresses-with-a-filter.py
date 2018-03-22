# Problem: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

import re

def fun(s):
    # return True if s is a valid email, else return False
    m = re.match(r'^[a-zA-Z0-9\-\_]+@[a-zA-Z0-9]+\..+$', s)
    res = True
    if m:
        n = re.search(r'\.\S+$', s)
        if len(n.group().replace('.', '', 1)) <= 3:
            res = True
        else:
            res = False
    else:
        res = False
    return res

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())


filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
