# Problem:

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print([1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111][i-1]*i)
