#%%
from collections import deque
r_m, c_m = 13, 12
readlines = [
    "0 0 0 0 0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 1 1 0 0 0",
    "0 1 1 1 0 0 0 1 1 0 0 0",
    "0 1 1 1 1 1 1 0 0 0 0 0",
    "0 1 1 1 1 1 0 1 1 0 0 0",
    "0 1 1 1 1 0 0 1 1 0 0 0",
    "0 0 1 1 0 0 0 1 1 0 0 0",
    "0 0 1 1 1 1 1 1 1 0 0 0",
    "0 0 1 1 1 1 1 1 1 0 0 0",
    "0 0 1 1 1 1 1 1 1 0 0 0",
    "0 0 1 1 1 1 1 1 1 0 0 0",
    "0 0 0 0 0 0 0 0 0 0 0 0",
    ]
foo= lambda x: 9 if x == '1' else 0 
arr = [list(map(foo,i.split())) for i in readlines]
arr = [i.split() for i in readlines]
arr
# %%
start = [(0,0)]
next=[]
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
                    arr[nr][nc] = res

    for rows in arr:
        if '0' in rows:
            return -1

    return res
    
bfs(start)
arr
# %%
