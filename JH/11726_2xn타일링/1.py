#%%
from math import comb

def a_(n):
    a_n = 0
    for i in range(0,(n//2+1)+1):
        a_n += comb(n-i,i)
    return(a_n)

n=int(input())
print(a_(n)%10007)
# %%
sum(1,2,3,)
# %%
