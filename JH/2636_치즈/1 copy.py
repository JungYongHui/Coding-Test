# #%%
# r_m, c_m = 13, 12
# readlines = [
#     "0 0 0 0 0 0 0 0 0 0 0 0",
#     "0 0 0 0 0 0 0 0 0 0 0 0",
#     "0 0 0 0 0 0 0 1 1 0 0 0",
#     "0 1 1 1 0 0 0 1 1 0 0 0",
#     "0 1 1 1 1 1 1 0 0 0 0 0",
#     "0 1 1 1 1 1 0 1 1 0 0 0",
#     "0 1 1 1 1 0 0 1 1 0 0 0",
#     "0 0 1 1 0 0 0 1 1 0 0 0",
#     "0 0 1 1 1 1 1 1 1 0 0 0",
#     "0 0 1 1 1 1 1 1 1 0 0 0",
#     "0 0 1 1 1 1 1 1 1 0 0 0",
#     "0 0 1 1 1 1 1 1 1 0 0 0",
#     "0 0 0 0 0 0 0 0 0 0 0 0",
#     ]
# inf = float("inf")
# inf = 9
# foo= lambda x: 1 if x == '1' else 0 
# arr = [
#     [inf] * (c_m+2),
#     *([inf, *map(foo,i.split()), inf] for i in readlines),
#     [inf] * (c_m+2)
#     ]
#%%
from sys import stdin

inf = float("inf")
foo= lambda x: 1 if x == '1' else 0 

r_m, c_m = map(int,input().split())
arr = [
    [inf] * (c_m+2),
    *([inf, *map(foo,i.split()), inf] for i in stdin.readlines()),
    [inf] * (c_m+2)
    ]

start = {(1,1)}
arr[1][1] = inf

next=[]
# 깊이 우선 탐색 함수 정의
def dfs(start):

    q=list(start)
    next = set()
    d_rc = ((1,0),(-1,0),(0,1),(0,-1))

    while q:
        r,c = q.pop()

        for d_r,d_c in d_rc:
            nr, nc = r+d_r, c+d_c
            v = arr[nr][nc]
            if not v:
                q.append((nr,nc))
                arr[nr][nc] = inf
            elif v == 1:
                next.add((nr,nc))

    for nr,nc in next:
        arr[nr][nc] = 0
    
    return next

cnt = 0

while True:
    next = dfs(start)
    if not next:
        print(cnt)
        print(len(start))
        break
    start = next
    cnt+=1
# %%