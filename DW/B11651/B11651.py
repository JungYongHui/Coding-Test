import sys

f_input = int(sys.stdin.readline())

data_list = []
for _ in range(f_input):
    s_input = tuple(map(int, sys.stdin.readline().split()))
    data_list.append(s_input)

# data_list.sort(key = lambda x:x[1])
# for i in data_list:
#     print(str(i)[1:-1].replace(',', ' '))