# 벽 3개를 설치해야함
# 그렇다면 어디에 설치해야 하는가?
# graph를 입력 받을때, 0(빈공간)의 좌표를 따로 저장해둔다
# -> 해당 좌표를 combination 해서 어느 빈 공간에 3개의 벽을 설치할지 정함

# 1. 조합(combination) 함수 생성 - 3개의 벽 좌표를 추출하는 함수
# ---- 조합의 총 개수 만큼 loop ----
# 2. 조합에서 추출된 좌표를 graph에 적용한 후 bfs 돌린 결과 뽑기
# ---- loop 끝 ----
# 3. max(안전영역) 구하기

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