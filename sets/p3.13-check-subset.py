# Problem: https://www.hackerrank.com/challenges/py-check-subset/problem

if __name__ == "__main__":
    T = int(input())
    for i in range(0, T):
        A_size = int(input())
        A = set(map(int, input().split()))
        B_size = int(input())
        B = set(map(int, input().split()))
        print(A.intersection(B) == A)
