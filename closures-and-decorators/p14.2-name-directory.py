# Problem: https://www.hackerrank.com/challenges/decorators-2-name-directory/problem

import operator

def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: int(x[2]))
        sorted_people = []
        for p in people:
            sorted_people.append(f(p))
        return sorted_people
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
