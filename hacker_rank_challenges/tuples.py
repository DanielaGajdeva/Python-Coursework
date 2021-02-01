# the code was copied from "Submitted code" field

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())

    print(hash(tuple(integer_list)))