# Problem: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    list = []

    i = 1
    while i <= N:
        command_string = input()
        commands = command_string.split()

        if commands[0] == 'insert':
            list.insert(int(commands[1]), int(commands[2]))
        elif commands[0] == 'print':
            print(list)
        elif commands[0] == 'remove':
            list.remove(int(commands[1]))
        elif commands[0] == 'append':
            list.append(int(commands[1]))
        elif commands[0] == 'sort':
            list.sort()
        elif commands[0] == 'pop':
            list.pop()
        elif commands[0] == 'reverse':
            list.reverse()
        i+=1
