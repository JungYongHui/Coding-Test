#%%
from sys import stdin
n,k = map(int,stdin.readline().split())
lst = list(map(int,stdin.readlines()))
ans = 0
for i in reversed(lst):
    q,r = divmod(k,i)
    ans += q
    k = r
print(ans)
# %%
