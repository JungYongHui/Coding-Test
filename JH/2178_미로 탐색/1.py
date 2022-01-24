#%%
from collections import deque
from sys import stdin

w,h = 4,6
map_ = [
    ['1','0','1','1','1','1',],
    ['1','0','1','0','1','0',],
    ['1','0','1','0','1','1',],
    ['1','1','1','0','1','1',],
    ]


w,h = map(int, input().split())
map_ = [list(stdin.readline().rstrip()) for _ in range(w)]

# print(*map_,sep='\n')
# print()

x_f,y_f = (w-1),(h-1)

visited = deque()

visited.append((0,0))
map_[0][0] = 1

d_xy = ((1,0),(-1,0),(0,-1),(0,1))

while map_[x_f][y_f]=='1':

    pos = visited.popleft()
    x,y = pos
    seq = map_[x][y]

    for d_x,d_y in d_xy:

        nx = x + d_x
        ny = y + d_y

        if 0<=nx<w and 0<=ny<h:
            if map_[nx][ny]=='1':
                # print(nx,ny)
                visited.append((nx,ny))
                map_[nx][ny] = seq + 1

    # print(*map_,sep='\n',end='\n\n')

# print(*map_,sep='\n')
# print(x_f,y_f)
print(repr(map_[x_f][y_f]))
# %%