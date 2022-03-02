import sys

def dfs(V):
    visited[V-1] = True
    print(V, end=" ")
    for i in range(1, N+1):
        if not visited[i-1] and graph[V-1][i-1] == 1:
            dfs(i)

def bfs(V):
    visited[V-1] = False
    queue = [V]
    while queue:
        V = queue.pop(0)
        print(V, end=" ")
        for i in range(1, N+1):
            if visited[i-1] and graph[V-1][i-1] == 1:
                queue.append(i)
                visited[i-1] = False

N, M, V = map(int, input().split())

graph = [[0]*(N) for _ in range(N)]
# graph (N=4인 경우)
#     1 2 3 4
# 1 [[0 1 1 1]
# 2 [1 0 0 1]
# 3 [1 0 0 1]
# 4 [1 1 1 0]]
visited = [False]*(N)
# visited = [False False False True]
# queue = []

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

dfs(V)
print()
bfs(V)