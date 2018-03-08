# Problem: https://www.hackerrank.com/challenges/no-idea/problem

if __name__ == "__main__":
    n, m = map(int, input().split())
    n_array = list(map(int, input().split()))
    A = set(list(map(int, input().split())))
    B = set(list(map(int, input().split())))

    initial_happiness = 0
    for i in n_array:
        if i in A:
            initial_happiness += 1
        if i in B:
            initial_happiness -= 1
    print(initial_happiness)
