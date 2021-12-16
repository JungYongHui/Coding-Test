# 백준 15552

# 덧셈
import sys

T = int(input()) # test case
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print('답:', a+b)


# 문자열
import sys

data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))