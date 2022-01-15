# 배낀거 (dp 정석 풀이)
import sys
input = sys.stdin.readline

n = int(input())
dt = list(map(int,input().split()))
dp = [0]*n
dp[0] = dt[0]
for i in range(1,n):
    if dp[i-1] < 0:
        dp[i] = dt[i]
    else:
        dp[i] = dp[i-1] + dt[i]

print(max(dp))