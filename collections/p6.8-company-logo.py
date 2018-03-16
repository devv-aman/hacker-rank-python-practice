# Problem: https://www.hackerrank.com/challenges/most-commons/problem
from collections import Counter

if __name__ == "__main__":
    s = dict(Counter(list(input().strip())))
    count = 1
    while True:
        max_value = max(s, key=s.get)
        max_values = [key for key in s.keys() if s[key] == s[max_value]]
        max_values.sort()
        for key in max_values:
            if count > 3:
                break
            print(key, s[key])
            del s[key]
            count += 1
        if count > 3:
            break
