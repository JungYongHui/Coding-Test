# %%
n=int(input())
dp = '0 '+input()

dp=list(map(int,dp.split()))

for i in range(n+1):
    candidate = []
    for j in range(i//2 + 1):
        candidate.append(dp[j]+dp[i-j])
    dp[i]=max(candidate)
    
print(dp[i])