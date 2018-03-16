# problem: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict
items = OrderedDict()
N = int(input())
for i in range(0, N):
    inp = input().split()
    price = int(inp[len(inp)-1])
    item_name = ''
    for j in range(0, len(inp)-1):
        if(j == len(inp)-2):
            item_name += str(inp[j])
        else:
            item_name += str(inp[j]) + ' '
    if item_name in items:
        items[item_name] = items[item_name] + price
    else:
        items[item_name] = price
for i in items:
    print(i, items[i])
