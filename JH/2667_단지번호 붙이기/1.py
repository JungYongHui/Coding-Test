#%%
# n=7
# map_ = [
#     "0110100",
#     "0110101",
#     "1110101",
#     "0000111",
#     "0100000",
#     "0111110",
#     "0111000",
#     ]


# print(*map_,sep="\n")

# n=7
# map_=[
#     [0, 1, 1, 0, 1, 0, 0],
#     [0, 1, 1, 0, 1, 0, 1],
#     [1, 1, 1, 0, 1, 0, 1],
#     [0, 0, 0, 0, 1, 1, 1],
#     [0, 1, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 0, 0, 0],
# ]
# [float('inf') if i=='1' else 0 for i in "0110100"]

#%%
from sys import stdin
n = int(stdin.readline())

map_ = [
    [1 if i=='1' else 0 for i in stdin.readline().rstrip()]
    for _ in range(n)
]

d_xy_lst = ((-1,0), (1,0), (0,1), (0,-1)) # 상하좌우

# bfs 구현
def bfs(x_, y_): # x_, y_: 시작노드
    queue_ = [(x_,y_)] #실제 큐로 구현하면 더 빠를 듯
    map_[x_][y_] = 2
    cnt = 0 # 아파트수 카운트

    while queue_:

        x, y = queue_[0]
        del queue_[0]
        cnt += 1

        for d_x, d_y in d_xy_lst:

            nx, ny = x+d_x, y+d_y

            if all((0<=nx<n , 0<=ny<n)):

                if map_[nx][ny] == 1:

                    map_[nx][ny] = 2
                    queue_.append((nx,ny))
    return cnt

arcades = []
for x in range(n):
    for y in range(n):
        if map_[x][y] == 1:
            arcades.append(bfs(x,y))

print(len(arcades))
print(*sorted(arcades),sep='\n')
# %%
