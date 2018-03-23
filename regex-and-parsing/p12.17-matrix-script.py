# Problem: https://www.hackerrank.com/challenges/matrix-script/problem

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
matrix = []
matrix_i = 0
for matrix_i in range(n):
    matrix_t = str(input().strip())
    matrix.append(matrix_t)

print(matrix)
# for i in range(m):
#     for j in range(n):
#         print(matrix[j][i])
