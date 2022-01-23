#%%
from sys import stdin
import queue

n = int(stdin.readline())
map_ = [
    [{'0':0, '1':1}[s] for s in stdin.readline().rstrip()]
    for _ in range(n)
    ]

d_xy_lst = ((-1,0), (1,0), (0,1), (0,-1)) # 상하좌우
#bfs용 큐
queue_ = queue.Queue()
# bfs 구현
def bfs(x_, y_): # x_, y_: 시작노드
    queue_.put((x_,y_))
    map_[x_][y_] = 0
    cnt = 0 # 아파트수 카운트

    while not queue_.empty():

        x, y = queue_.get()
        cnt += 1

        for d_x, d_y in d_xy_lst:

            nx, ny = x+d_x, y+d_y

            if all((0<=nx<n , 0<=ny<n)):

                if map_[nx][ny]:

                    map_[nx][ny] = 0
                    queue_.put((nx,ny))
    return cnt

arcades = []
for x in range(n):
    for y in range(n):
        if map_[x][y]:
            arcades.append(bfs(x,y))
            
print(len(arcades))
print(*sorted(arcades),sep='\n')
#%%
