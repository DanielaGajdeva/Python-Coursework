# the code was copied from "Submitted code" field
# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(raw_input())
    my_list = []

    for i in range(N):
        parameters = list(raw_input().split())

        if len(parameters) == 1:
            if parameters[0] == "print":
                print(my_list)
            elif parameters[0] == "pop":
                my_list.pop()
            elif parameters[0] == "reverse":
                my_list.reverse()
            elif parameters[0] == "sort":
                my_list.sort()
        elif len(parameters) == 2:
            if parameters[0] == "remove":
                my_list.remove(int(parameters[1]))
            elif parameters[0] == "append":
                my_list.append(int(parameters[1]))
        else:
            if parameters[0] == "insert":
                my_list.insert(int(parameters[1]), int(parameters[2]))
