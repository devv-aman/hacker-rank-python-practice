# Problem: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

if __name__ == "__main__":
    A = set(map(int, input().split()))
    n = int(input())
    output = True
    for i in range(0,  n):
        other_set = set(map(int, input().split()))
        if other_set.intersection(A) != other_set:
            output = False
            break
    print(output)
