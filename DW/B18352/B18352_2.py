import sys
from collections import deque

input = sys.stdin.readline
# 도시의 개수 / 도로의 개수 / 거리 정보 / 출발 도시
n, m, k, x = map(int, input().split())

# 간선 저장 / 인덱스 == 도시
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
def bfs(x):
    # 첫 스타트
    visited = [False] * (n+1)
    distance = [0] * (n+1)
    answer = []
    
    que = deque([x])
    visited[x] = True
    distance[x] = 0
    
    # 탐색 시작(bfs)
    while que:
        now = que.popleft()
        for nxt in graph[now]:
            if not visited[nxt]: # 만약 방문 안했다면
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
        