# 벽 3개를 설치해야함
# 그렇다면 어디에 설치해야 하는가?
# graph를 입력 받을때, 0(빈공간)의 좌표를 따로 저장해둔다
# -> 해당 좌표를 combination 해서 어느 빈 공간에 3개의 벽을 설치할지 정함

# 1. 조합(combination) 함수 생성 - 3개의 벽 좌표를 추출하는 함수
# ---- 조합의 총 개수 만큼 loop ----
# 2. 조합에서 추출된 좌표를 graph에 적용한 후 bfs 돌린 결과 뽑기
# ---- loop 끝 ----
# 3. max(안전영역) 구하기

# 입력값 받기
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

EMPTY = 0
WALL = 1
VIRUS = 2
empty_list = []
virus_list = []

# 빈 공간, virus 좌표 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] == EMPTY:
            empty_list.append((i, j))
        elif graph[i][j] == VIRUS:
            virus_list.append((i, j))

# graph를 임시로 저장할 임시 graph
temp = [[0]*m for _ in range(n)]


def combination():

