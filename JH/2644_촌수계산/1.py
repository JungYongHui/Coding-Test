#%%
n_max = 9
start, end = 7, 3
n_line = 7
lines= [
    (1, 2),
    (1, 3),
    (2, 7),
    (2, 8),
    (2, 9),
    (4, 5),
    (4, 6),
    ]

map_ = [[0]*n_max for _ in range(n_max)]
for line in lines:
    r,c = line[0]-1, line[1]-1
    map_[r][c] = 1
    map_[c][r] = 1

print(*map_, sep="\n")
# %% bfs
def bfs():
    visited = []
    
