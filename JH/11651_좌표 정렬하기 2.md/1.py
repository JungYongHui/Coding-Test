#%%
import sys
input = sys.stdin.readline

iteration = int(input())

lst=[]
for i in range(iteration):
    xy = input().split()
    lst.append(xy)

key = lambda x: (int(x[1]),int(x[0]))

lst.sort(key=key)
for xy in lst:
    print(*xy)
# %%
