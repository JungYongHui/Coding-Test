import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = input().split()
graph = [[] for i in range(n+1)] # python index 번호 때문

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
def bfs(start):
    visited = [False] * (n+1)
    distance = [0] * (n+1)
    answer = []
    
    que = deque([start])
    visited[start] = True
    distance[start] = 0
    while que:
        now = que.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                distance[nxt] = distance[now] + 1
                que.append(nxt)
                
                if distance[nxt] == k:
                    answer.append(nxt)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end = '\n')
            
bfs(x)
        