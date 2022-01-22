# %%
from sys import stdin
n = int(stdin.readline())

dp=[[0] for _ in range(n+1)]
max_ = 0

for i in range(1, n+1):
    period, pay = map(int,stdin.readline().split())
    start, end = i, i+period-1
    
    max_ = max(*dp[start-1],max_)

    if end <= n:
        pay = max_ + pay
        dp[end].append(pay)

print(max(max_,max(dp[n])))
