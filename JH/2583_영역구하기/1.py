from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()
m, n, k = 5, 7, 3
ls=[
    [0, 2, 4, 4],
    [1, 1, 2, 5],
    [4, 0, 6, 2],
    ]

m,n,k = map(int,input().split())
ls= ([*map(int,input().split())] for i in range(k))
# print(m,n,k)
# print(*ls)
map_= [[1]*m for _ in range(n)]
ans=[]

for l in ls:
    for x in range(l[0],l[2]):
        for y in range(l[1],l[3]):
            map_[x][y]=0

for i in range(m*n):
    start = divmod(i,m)

    if map_[start[0]][start[1]]==0:
        continue

    visited = deque([start])
    map_[start[0]][start[1]] = 0

    d_xy = ((1,0), (-1,0), (0,1), (0,-1))
    cnt = 1

    while visited:
        x,y = visited.popleft()
        
        for d_x,d_y in d_xy:
            
            nx, ny = x + d_x, y + d_y

            if all((0<=nx<n, 0<=ny<m)):

                if map_[nx][ny]:
                    cnt+=1
                    map_[nx][ny]=0
                    visited.append((nx,ny))

    ans.append(cnt)
print(len(ans))
print(*sorted(ans))