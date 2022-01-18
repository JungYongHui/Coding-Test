# %%
from sys import stdin

n=int(input())
arr = (tuple(map(int,i.split())) for i in stdin.readlines())

arr = sorted(arr)
lst = [arr[0][1]]

for i,j in arr[1:]:
    if lst[-1] <= i:
        lst.append(j)
    elif lst[-1] > j:
        lst[-1] = j

print(len(lst))
# %%
