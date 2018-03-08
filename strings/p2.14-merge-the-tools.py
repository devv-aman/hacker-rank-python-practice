# Problem: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    #divide the string

    # AABCAAADASHS
    string_list = []
    for i in range(0, int(n/k)):
        string_list.append(string[k*i:k*i+k])
    for index, value in enumerate(string_list):
        ui = value
        while True:
            flag = 0
            for i in range(1, len(ui)):
                pos =  ui[0:i].find(ui[i])
                if pos != -1:
                    ui = ui[0:i] + ui[i+1:len(ui)]
                    flag = 1
                    break
            if flag == 0:
                break
        print(ui)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
