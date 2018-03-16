# Problem: https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations

if __name__ == "__main__":
    N = int(input())
    alpha_list = list(input().split())
    K = int(input())

    index_of_a = [i+1 for i, x in enumerate(alpha_list) if x == 'a']
    total_combinations = list(combinations(alpha_list, K))
    num = 0
    for i in total_combinations:
        if 'a' in i:
            num += 1

    print(num/len(total_combinations))
