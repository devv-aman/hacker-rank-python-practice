# Problem: https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

import re

def wrapper(f):
    def fun(l):
        mobile_list = []
        for mobile in l:
            if len(mobile) > 10:
                mobile = re.sub(r'^0|^91|^\+91', '', mobile)
            mobile_list.append(mobile)
        mobile_list.sort()
        mobile_list = ['+91 ' + x[:5] + " " + x[5:] for x in mobile_list]
        f(mobile_list)
        return mobile_list
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
