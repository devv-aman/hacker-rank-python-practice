# Problem: https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    index, count = 0, 0
    while True:
        index = string.find(sub_string, index)
        if index == -1:
            break

        count += 1
        index += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
