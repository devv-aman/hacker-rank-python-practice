# Problem: https://www.hackerrank.com/challenges/py-set-union/problem

if __name__ == "__main__":
    n = int(input())
    roll_number_english_list = set(map(int, input().split()))
    b = int(input())
    roll_number_french_list = set(map(int, input().split()))

    print(len(roll_number_english_list.union(roll_number_french_list)))
