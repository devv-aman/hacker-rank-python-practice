# Problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    no_of_commands = int(input())

    for i in range(0, no_of_commands):
        command_str = input()
        command_arr = command_str.split()
        if command_arr[0] == 'pop':
            s.pop()
        elif command_arr[0] == 'remove':
            if int(command_arr[1]) in list(s):
                s.remove(int(command_arr[1]))
        elif command_arr[0] == 'discard':
            s.discard(int(command_arr[1]))
    print(sum(s))
