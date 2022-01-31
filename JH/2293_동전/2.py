#%%
n,k = 3,4
coins=[2,5,1]
from sys import stdin
n,k = map(int, input().split())
coins = [int(i) for i in stdin.readlines()]

arr = [0]*(k+1)

i = 0
coin = coins[i]
#
for i in range(1,k+1):
    if i % coin == 0:
        arr[i] = 1
#
for i in range(1,n):
    coin = coins[i]
    if coin > k:
        continue

    i = coin
    arr[i] += 1

    for i in range(coin+1,k+1):
        arr[i] += arr[i-coin]

print(arr[-1])
# %%