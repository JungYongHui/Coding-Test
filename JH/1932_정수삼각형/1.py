from sys import stdin

input = lambda: stdin.readline().rstrip()

n = int(input())
dp = [int(input())]

for _ in range(n-1):
    l = list(map(int,input().split()))
    dp = [max(dp[max(0,i-1):i+1])+k for i, k in enumerate(l)]
    # print(dp)
print(max(dp))