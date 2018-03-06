# Problem: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    # your code goes here
    for i in range(1, size+1):
        index = (97 + size - i)
        alpha = chr(index)
        for j in range(1, i):
            alpha = chr(index+j) + '-' + alpha
        for j in range(1, i):
            alpha =  alpha + '-' + chr(index+j)
        print(alpha.center((4*size - 3), '-'))

    for i in range(1, size):
        index = (97 + i)
        alpha = chr(index)
        for j in range(1, size-i):
            alpha = chr(index+j) + '-' + alpha
        for j in range(1, size-i):
                alpha = alpha + '-' + chr(index+j)
        print(alpha.center((4*size - 3), '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
