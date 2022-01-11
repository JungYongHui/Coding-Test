import sys

def number_card():
    f_input_num = int(sys.stdin.readline())
    f_input_set = set(sys.stdin.readline().split())

    s_input_num = int(sys.stdin.readline())
    s_input_list = list(sys.stdin.readline().split())

    for i in s_input_list:
        if i in f_input_set:
            yield 1
        else:
            yield 0

print(*number_card())
