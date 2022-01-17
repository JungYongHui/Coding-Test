import sys

f_input = int(sys.stdin.readline())
s_input = set(sys.stdin.readline().split())

answer = sorted(s_input)
for i in answer:
    print(i, sep=' ', end=' ')