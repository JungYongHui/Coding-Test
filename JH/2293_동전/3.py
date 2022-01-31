#%%
n,k = 3,10
coins=[2,5,1]
from sys import stdin
n,k = map(int, input().split())
coins = [int(i) for i in stdin.readlines()]

arr = [1]+[0]*(k)
for coin in coins:
    for i in range(coin,k+1):
        if not arr[i-coin]:
            continue
        arr[i] += arr[i-coin]

print(arr[-1])
# %%