# Problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem

if __name__ == "__main__":
    K = int(input())
    list_of_room_numers = list(map(int, input().split()))
    for i in set(list_of_room_numers):
        list_of_room_numers.remove(i)
        if i not in list_of_room_numers:
            print(i)
            break
