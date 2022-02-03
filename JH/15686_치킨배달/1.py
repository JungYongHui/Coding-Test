#%%
N,M = 5, 3
map_=[
    [0, 0, 1, 0, 0,],
    [0, 0, 2, 0, 1,],
    [0, 1, 2, 0, 0,],
    [0, 0, 1, 0, 0,],
    [0, 0, 0, 0, 2,],
    ]
#%%
from sys import stdin
from itertools import combinations
N,M = map(int,input().split())
map_=[list(map(int,stdin.readline().split())) for _ in range(N)]

h_l=[]
c_l=[]
for r in range(N):
    for c in range(N):
        v = map_[r][c]
        if v==1:
            h_l.append((r,c))
        elif v==2: 
            c_l.append((r,c))

arr=[[0]*len(c_l) for _ in range(len(h_l))]
arr

i,j=0,0
for h_x,h_y in h_l:
    for c_x,c_y in c_l:
        arr[i][j]=(abs(h_x-c_x)+abs(h_y-c_y))
        j+=1
    j=0
    i+=1

def c_d(arr,m):
    n_c = len(arr[0])
    ans=float('inf')
    for t in combinations({*range(n_c)},m):
        pick = lambda h: [h[i] for i in t]
        ans_=sum(map(min,(map(pick,arr))))
        ans = min(ans,ans_)
    return ans
print(c_d(arr,M))
# %%