#%%
n=int(input())
dp = '0 '+input()

dp=list(map(int,dp.split()))

for i in range(n+1):
    dp[i] = max(dp[j]+dp[i-j] for j in range(i//2 + 1))
    
print(dp[i])