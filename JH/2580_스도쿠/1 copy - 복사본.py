#%%
"""
1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1
"""
sdk = [
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,],
]

# sdk=[
#     [0, 3, 5, 4, 6, 9, 2, 7, 8],
#     [7, 8, 2, 1, 0, 5, 6, 0, 9],
#     [0, 6, 0, 2, 7, 8, 1, 3, 5],
#     [3, 2, 1, 0, 4, 6, 8, 9, 7],
#     [8, 0, 4, 9, 1, 3, 5, 0, 6],
#     [5, 9, 6, 8, 2, 0, 4, 1, 3],
#     [9, 1, 7, 6, 5, 2, 0, 8, 0],
#     [6, 0, 3, 7, 0, 1, 9, 5, 2],
#     [2, 5, 8, 3, 9, 4, 7, 6, 0],
#     ]

# from sys import stdin
# sdk = [list(map(int,i.split())) for i in stdin.readlines()]
loc=[]
available_set=[]
realation_set=[]
res=[]
for r in range(9):
    for c in range(9):
        if not sdk[r][c]:
            #1
            set_=set()
            for i,pos in enumerate(loc):
                if (r == pos[0]) or (c == pos[1]):
                    set_.add(i)
            realation_set.append(set_)                
            #2
            set_={*range(1,10)}.difference(set(sdk[r]),{row[c] for row in sdk})
            available_set.append(set_)
            #3
            loc.append((r,c))
            #4
            res.append(0)
print(loc)
print(available_set)
print(realation_set)
# %%

set_ = set(range(1,10))
def check(x,num):
    if num in (res[x_] for x_ in realation_set[x]):
            return False
    return True

def sol(x):
    global res
    if x == len(res):
        # print('!')
        return res

    for i in available_set[x]:
        if check(x,i):
            res[x] = i
            # print(x,res)
            sol(x+1)

sol(0)
#%%
for i,num in enumerate(res):
    r,c = loc[i]
    sdk[r][c] = num

for row in sdk:
    print(*row)
# %%
