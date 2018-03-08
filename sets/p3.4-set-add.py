# Problem: https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == "__main__":
    N = input()
    N = int(N)
    stamp_set = set()
    for i in range(0, N):
        stamp_set.add(input())
    print(len(stamp_set))
