# Problem: https://www.hackerrank.com/challenges/py-set-mutations/problem

if __name__ == "__main__":
    n = int(input())
    A = set(map(int, input().split()))
    N = int(input())
    for i in range(0, N):
        command_str = input()
        command_arr = command_str.split()
        operation_set = set(map(int, input().split()))
        if command_arr[0] == 'update':
            A.update(operation_set)
        elif command_arr[0] == 'intersection_update':
            A.intersection_update(operation_set)
        elif command_arr[0] == 'difference_update':
            A.difference_update(operation_set)
        elif command_arr[0] == 'symmetric_difference_update':
            A.symmetric_difference_update(operation_set)
    print(sum(A))
