# Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == '__main__':
    N = int(input())
    N_list = list(map(int, input().split()))
    M = int(input())
    M_list = list(map(int, input().split()))

    N_set = set(N_list)
    M_set = set(M_list)

    symmetric_difference = list(N_set.difference(M_set))
    symmetric_difference += list(M_set.difference(N_set))
    symmetric_difference.sort()
    for i in symmetric_difference:
        print(i)
