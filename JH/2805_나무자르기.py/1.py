from sys import stdin
input = stdin.readline

n, target = (int(i) for i in input().split())
trees  = [int(i) for i in input().split()]
# %%
l, r = 0, 1_000_000_000

while l <= r:
    mid = (l + r)//2
    
    if sum(c for tree in trees if (c:=tree-mid)>0) >= target:
        l = mid +1
    else:
        r = mid -1
        
print(r)
#%%
# [c for tree in trees if (c:=tree-mid)>0]