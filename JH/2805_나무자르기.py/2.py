from sys import stdin
input = stdin.readline

from collections import Counter

n, target = map(int,input().split())
trees  = Counter(map(int,input().split()))
# %%
l, r = 0, max(trees)

while l <= r:
    mid = (l + r)//2
    
    if sum(c*j for i,j in trees.items() if (c:=i-mid)>0) >= target:
        l = mid +1
    else:
        r = mid -1
        
print(r)