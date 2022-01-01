#%% 베낀건데 제일 깔끔한 풀이같음
X = int(input())
cache = {1 : 0, 2 : 1}

def dp(n):
    if n in cache:
        return cache[n]
    
    cnt = 1 + min(dp(n // 3) + n % 3, dp(n // 2) + n % 2)
    cache[n] = cnt
    return cnt

print(dp(X))