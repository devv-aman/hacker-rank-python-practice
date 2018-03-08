# Problem: https://www.hackerrank.com/challenges/capitalize/problem

import re

def capitalize(string):
    #Hello   World  Lol
    iter = re.finditer(r"\w+\s*", string)
    indices = [m.start(0) for m in iter]
    capitalized_string = ''
    for i, value in enumerate(indices):
        if i+1 == len(indices):
            capitalized_string += string[value].upper() + string[value+1:len(string)]
        else:
            capitalized_string += string[value].upper() + string[value+1:indices[i+1]]
    return capitalized_string



if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
