# Problem: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(0, n):
        a.append(input())
    for i in range(0, m):
        b.append(input())

    for i in b:
        flag = 0
        for j, x in enumerate(a):
            if(x == i):
                print(j+1, end = ' ')
                flag = 1
        if(flag == 0):
            print('-1', end = '')
        print('')
