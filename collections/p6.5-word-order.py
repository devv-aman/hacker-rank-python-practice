# Problem: https://www.hackerrank.com/challenges/word-order/problem

from collections import Counter, OrderedDict

n = int(input())
word_list = OrderedDict()

for i in range(0, n):
    word = input()
    if word in word_list:
        word_list[word] += 1
    else:
        word_list[word] = 1
print(len(list(word_list)))
for i in word_list:
    print(word_list[i], end = ' ')
