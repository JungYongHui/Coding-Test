#%%
n=7
map_ = [
    "0110100",
    "0110101",
    "1110101",
    "0000111",
    "0100000",
    "0111110",
    "0111000",
    ]
from sys import stdin
n = int(stdin.readline())
[float('inf') if i=='1' else 0 for i in "0110100"]
map_ = [
    [1 if i=='1' else 0 for i in stdin.readline().rstrip()]
    for _ in range(n)
]
print(*map_,sep="\n")
# %%
n=7
map_=[
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0],
]

d_pos_lst = ((-1,0), (1,0), (0,1), (0,-1)) # 상하좌우

for x in range(n):
    for y in range(n):
        pos = x,y
