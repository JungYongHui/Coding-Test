#%% 
mod = 10_007
N = int(input())
# N = 2

dp =[0] * max(3,N+1)
dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
    dp[i] = (dp[i-1] + 2*dp[i-2]) % mod

print(dp[N])
# %%
