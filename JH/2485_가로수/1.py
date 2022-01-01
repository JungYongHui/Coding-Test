# %%
from math import gcd
from sys import stdin
input = stdin.readline

N = int(input())

old = int(input())
new = int(input())
tmp_gcd = new-old

start = old
old = new

for _ in range(2, N):
    new = int(input())
    dist = new-old
    tmp_gcd = gcd(tmp_gcd,dist)
    
    old = new

end = old

ans = ((end-start)//tmp_gcd)-(N-1)
print(ans)
#%%

