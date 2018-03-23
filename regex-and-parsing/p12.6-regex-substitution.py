# Problem: https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
import re

N = int(input())
text = ''
for i in range(N):
    if i == N-1:
        text += input()
    else:
        text += input() + '\n'

while True:
    originaltext = text
    text = re.sub("(\s\&\&\s)", " and ", text)
    if text == originaltext:
        break

while True:
    originaltext = text
    text = re.sub("(\s\|\|\s)", " or ", text)
    if text == originaltext:
        break
print(text)
