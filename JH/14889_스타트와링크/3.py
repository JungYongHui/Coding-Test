# 베낀거
#%% 172ms로 엄청 빠름(내껀 1000ms)
import sys; input = sys.stdin.readline
from itertools import combinations

n = int(input())

S = [list(map(int, input().split())) for _ in range(n)]
row, col = [sum(i) for i in S], [sum(i) for i in zip(*S)]
new_S = [i+j for i, j in zip(row, col)]
total_sum = sum(new_S) // 2

ans = float('inf')
for combi in combinations(new_S, n//2):
    ans = min(ans, abs(total_sum - sum(combi)))

    if not ans:
        break

print(ans)