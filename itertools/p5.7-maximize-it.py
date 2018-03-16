# Problem: https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product

if __name__ == "__main__":
    K, M = input().split()
    K, M = int(K), int(M)

    list_of_lists = []
    for i in range(0, K):
        inp = list(map(int, input().split()))
        list_of_lists.append(inp[1:])

    product_list = list(product(*list_of_lists))
    sums = []

    for i in product_list:
        t_sum = 0
        for j in i:
            t_sum += int(j) ** 2
        sums.append(t_sum % M)

    print(max(sums))
