# Problem: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    # your code goes here

    vowels = ['A', 'E', 'I', 'O', 'U']
    vowels_substring = {}
    consonant_substring = {}
    kevin_score = 0
    stuart_score = 0

    for i in range(0, len(string)):
        index = string.find(string[i], i)
        if string[i] in vowels:
            vowels_substring[index] = string[i]
        else:
            consonant_substring[index] = string[i]
    for key in vowels_substring:
        kevin_score += (len(string) - int(key))
    for key in consonant_substring:
        stuart_score += (len(string) - int(key))

    if kevin_score > stuart_score:
        print('Kevin', kevin_score)
    elif stuart_score > kevin_score:
        print('Stuart', stuart_score)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
