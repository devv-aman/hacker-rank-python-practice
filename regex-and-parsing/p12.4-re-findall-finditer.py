# Problem: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re
s = input()
matches = re.finditer(r'([AEIOUaeiou])+', s)
flag = 0
words = []
for x in matches:
    word = x.group()
    if len(word) >= 2:
        words.append(word)
        flag = 1

if re.search(r'([AEIOUaeiou][AEIOUaeiou]+$)', s):
    words = words[:len(words)-1]
if re.search(r'^([AEIOUaeiou][AEIOUaeiou]+)', s):
    words = words[1:]

if len(words) != 0:
    [print(word) for word in words]
if flag == 0:
    print(-1)
