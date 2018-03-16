# Problem: https://www.hackerrank.com/challenges/piling-up/problem

for t in range(int(input())):
    n = int(input())
    side_lengths = list(map(int, input().split()))
    if(max(side_lengths) not in [side_lengths[0], side_lengths[-1]]):
        print("No")
    else:
        print("Yes")
