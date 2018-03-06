# Problem: https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()

    # str.isalnum() = checks if all the characters of a string are alphanumeric
    # str.isalpha() = checks if all the characters of a string are alphabetical
    # str.isdigit() = are digits
    # str.islower() = are lowercase characters
    # str.isupper() = are uppercase characters
    # qA2
    output_list = [False, False, False, False, False]
    for i in range(0, len(s)):
        if s[i].isalnum():
            output_list[0] = True
        if s[i].isalpha():
            output_list[1] = True
        if s[i].isdigit():
            output_list[2] = True
        if s[i].islower():
            output_list[3] = True
        if s[i].isupper():
            output_list[4] = True

    for i in output_list:
        print(i)
