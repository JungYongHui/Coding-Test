import sys


# 0  1  2  3  4  5  6 ...

# 1, 1, 2, 3, 5, 8, 13 ... == d

memo = [0 for _ in range(101)]

def dp(n):
    ######
    # memozation
    ######
    if memo[n] != 0: # 저장이 되어 있다면
        return memo[n]
    
    # if n <= 2: 
    #     memo[n] = 1
    #     return memo[n]
    
    if n == 1:
        memo[n] = 1
        return memo[n]
    
    if n == 2:
        memo[n] = 2
        return memo[n]
    
    
    else: # 3이상이면
        memo[n] = (dp(n-1) + dp(n-2)) % 10007
        return memo[n] 
    
input = sys.stdin.readline
print(dp(int(input().rstrip())))
for i in memo:
    if i != 0:
        print(i, end = ' ')