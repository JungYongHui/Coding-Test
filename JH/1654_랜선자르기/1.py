#%%
k=4
n=11
lines = [802,743,457,539]
l = 0
r = 2**23-1
a = (l+r)//2
#%%
from sys import stdin
k,n = map(int,input().split())
lines = list(map(int,stdin.readlines()))
l = 0
r = 2**31
# print(lines)
def foo(a):
    s = sum(line//a for line in lines)
    if s >= n:
        return True
    else:
        return False

while l <= r:
    a = (l+r)//2
    if foo(a):
        l = a+1
    else:
        r = a-1
    # print(l,r,a)

print(r)
# %%
int(2147483647)
# %%
2**31-2