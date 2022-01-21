#%%
n = 7
inputs = [
    "3 10",
    "5 20",
    "1 10",
    "1 20",
    "2 15",
    "4 40",
    "2 200",
]

# %%
from sys import stdin
n = int(stdin.readline())
ans = 0
dp=[[0] for _ in range(20)]
for i in range(n):
    period, pay = map(int,stdin.readline().split())
    start, end = i, i+period-1
    if end < n:
        pay = pay+dp[i][0]
        dp[end].append(pay)
        ans = max(ans,pay)
    dp[i]=[max(dp[i])]
print(dp)
print(ans)
#%%

# %%
