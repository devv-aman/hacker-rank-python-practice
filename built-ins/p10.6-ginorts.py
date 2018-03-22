# Problem: https://www.hackerrank.com/challenges/ginorts/problem
# Unable to solve by myself, found the solution from the discussion tab

import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')
