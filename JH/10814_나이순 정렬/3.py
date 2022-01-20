#%% (베낀거) 제일 깔끔한듯
import sys

input = sys.stdin.readline

N = int(input())

li = [input() for _ in range(N)]

li.sort(key=lambda x: int(x.split()[0]))

print(''.join(li))