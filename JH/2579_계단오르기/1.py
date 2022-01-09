#%%
from sys import stdin
input = lambda: int(stdin.readline())

step = input()
dp = [None for _ in range(step+1)]
dp[0]=(0,0)
dp[1]=tuple([input()]*2)
for i in range(2,step+1):
    score = input()
    dp[i] = (dp[i-1][1]+score, max(dp[i-2])+score)

print(max(dp.pop()))
#%%
