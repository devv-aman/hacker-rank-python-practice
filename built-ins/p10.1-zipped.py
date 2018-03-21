# Problem: https://www.hackerrank.com/challenges/zipped/problem

N, X = map(int, input().split())
list_of_marks = []

for i in range(X):
    list_of_marks.append(list(map(float, input().split())))

for i in zip(*list_of_marks):
    print("%.1f" % round(sum(list(i)) / len(list(i)),1))
