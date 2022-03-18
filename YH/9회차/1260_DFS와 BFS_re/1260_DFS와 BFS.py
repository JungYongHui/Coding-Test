from collections import deque

# 입력값 받기
n, m, s = map(int, input().split()) # 정점, 간선, 시작 정점
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
    graph[y - 1][x - 1] = 1
visited = [False * n]

def dfs(node, visited):
    visited[node - 1] = True
    print(node, ' ')
    for _ in range(1, n+1):



