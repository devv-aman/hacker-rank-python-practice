# Problem: https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):

    swapped_string = ''

    for x in s:
        if x.islower():
            swapped_string = swapped_string + x.upper()
        else:
            swapped_string = swapped_string + x.lower()
    return swapped_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
