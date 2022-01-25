import sys


f_input = int(sys.stdin.readline())
array = []
for _ in range(f_input):
    s_input = tuple(map(int, sys.stdin.readline().split()))
    array.append(s_input)

array = sorted(array, key=lambda x:x[1])
for i in array:
    print(i[0], i[1])