from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

temp = [[0]*m for _ in range(n)]

VIRUS = 2
WALL = 1
EMPTY = 0

vir_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == VIRUS:
            vir_list.append((i, j))

dx = [-1, 0 ,1, 0]
dy = [0, -1, 0, 1]

result = 0

def bfs(row, col):
    queue = deque()
    queue.append((row, col))

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            n_r = row + dx[i]
            n_c = col + dy[i]

            if n_r >= 0 and n_r < n and n_c >= 0 and n_c < m:
                if temp[n_r][n_c] == EMPTY:
                    temp[n_r][n_c] = VIRUS
                    queue.append((n_r, n_c))

def score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == EMPTY:
                score += 1
    return score

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]

        for i, j in vir_list:
            bfs(i, j)

        result = max(result, score())
        return True

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1


dfs(0)
print(result)