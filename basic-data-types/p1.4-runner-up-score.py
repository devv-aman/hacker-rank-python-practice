# Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = list(set(arr))
    arr.sort()

    print(arr[-2])
    # print(arr)
    # max_index = arr.index(max(arr))
    # del arr[max_index]
    # print(arr)
    # max_index = arr.index(max(arr))
    # print(arr[max_index])
