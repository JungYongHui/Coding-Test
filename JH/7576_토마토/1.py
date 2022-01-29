#%%
c_m,r_m = 6,4
arr = [
    ['0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '1'],
    ]
# %%
from collections import deque
from sys import stdin
# input
c_m,r_m = map(int,input().split())
arr=[stdin.readline().split() for _ in range(r_m)]
# 시작위치 결정
start = []
for i in range(r_m):
    for j in range(c_m):
        if arr[i][j]=='1':
            start.append((i,j))
# 너비 우선 탐색 함수 정의
def bfs(start):

    q=deque(start)
    for r,c in start:
        arr[r][c] = 0

    d_rc = ((1,0),(-1,0),(0,1),(0,-1))
    res = 0

    while q:
        r,c = q.popleft()
        res = arr[r][c]

        for d_r,d_c in d_rc:
            nr, nc = r+d_r, c+d_c
            if 0<=nr<r_m and 0<=nc<c_m:
                if arr[nr][nc] == '0':
                    q.append((nr,nc))
                    arr[nr][nc] = res+1

    for rows in arr:
        if '0' in rows:
            return -1

    return res

print(bfs(start))