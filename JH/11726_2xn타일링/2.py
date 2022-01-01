# 다이나믹 프로그래밍으로 푼 예제(베낀거)
mod = 10_007
N = int(input())
dp =[1] * (N+1)

for i in range(2, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % mod
print(dp[N])
