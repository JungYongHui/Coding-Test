from collections import deque
import sys

n, m, v = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    # x, y = map(int, input().split())
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1][y-1] = graph[y-1][x-1] = 1

visited = [False] * n

def dfs(v):
    visited[v-1] = True
    print(v, end=' ')

    for v_n in range(len(graph[v-1])):
        if graph[v-1][v_n] == 1 and visited[v_n] == False:
            dfs(v_n+1)


def bfs(start_v, visited):
    deq = deque()
    deq.append(start_v)
    visited[start_v-1] = True

    while deq:
        v = deq.popleft()
        print(v, end=' ')

        for n_v in range(len(graph[v-1])):
            if graph[v-1][n_v] == 1 and visited[n_v] == False:
                deq.append(n_v+1)
                visited[n_v] = True

dfs(v)
print()
bfs(v, [False]*n)