#%%
n,k = 3,10
coins=[1,2,5]

from sys import stdin
n,k = map(int, input().split())
coins = [int(i) for i in stdin.readlines()]

cnt=0
def foo(arr1,k):
    global cnt
    if not k:
        cnt+=1
        return 
    elif not arr1:
        return

    # *arr2, coin = arr1
    coin = arr1[-1]
    # arr2=arr1
    
    for i in range(k//coin + 1):
        val = i*coin
        foo(arr1[:-1],k-val)

ans=[]
foo(coins,k)
print(cnt)
# %%
