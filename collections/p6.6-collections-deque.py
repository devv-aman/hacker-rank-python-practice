# Problem: https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque
d = deque()
N = int(input())
for i in range(0, N):
    command_str = input()
    if ' ' in command_str:
        command, value = command_str.split()
    else:
        command = command_str
    if(command == 'append'):
        d.append(int(value))
    elif(command == 'pop'):
        d.pop()
    elif(command == 'popleft'):
        d.popleft()
    elif(command == 'appendleft'):
        d.appendleft(int(value))
[print(i, end = ' ') for i in d]
