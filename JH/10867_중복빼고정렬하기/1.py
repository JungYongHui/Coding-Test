#%%
from sys import stdin
input = stdin.readline
#%%
n = input()
input_set = set(input().split())
input_lst = sorted(input_set, key=int)
print(*input_lst)

