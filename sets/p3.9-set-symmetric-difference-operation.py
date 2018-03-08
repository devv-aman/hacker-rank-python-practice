# Problem: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

if __name__ == "__main__":
    n = int(input())
    roll_number_english_list = set(map(int, input().split()))
    b = int(input())
    roll_number_french_list = set(map(int, input().split()))

    print(len(roll_number_english_list.symmetric_difference(roll_number_french_list)))
