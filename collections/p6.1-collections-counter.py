# Problem: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == "__main__":
    X = int(input())
    shoe_sizes = list(map(int, input().split()))
    N = int(input())

    amount = 0
    for i in range(0, N):
        shoe_size, price = input().split()
        shoe_size, price = int(shoe_size), int(price)

        if shoe_size in shoe_sizes:
            amount += price
            shoe_sizes.remove(shoe_size)

    print(amount)
