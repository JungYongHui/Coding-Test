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

sdk=[
    [0, 3, 5, 4, 6, 9, 2, 7, 8],
    [7, 8, 2, 1, 0, 5, 6, 0, 9],
    [0, 6, 0, 2, 7, 8, 1, 3, 5],
    [3, 2, 1, 0, 4, 6, 8, 9, 7],
    [8, 0, 4, 9, 1, 3, 5, 0, 6],
    [5, 9, 6, 8, 2, 0, 4, 1, 3],
    [9, 1, 7, 6, 5, 2, 0, 8, 0],
    [6, 0, 3, 7, 0, 1, 9, 5, 2],
    [2, 5, 8, 3, 9, 4, 7, 6, 0],
    ]
loc=[]
vals=[]
for r in range(9):
    for c in range(9):
        if not sdk[r][c]:
            loc.append((r,c))
            vals.append(0)

# %%
set_ = set(range(1,10))
def check(r,c):
    if set(sdk[r]) == set_ == {row[c] for row in sdk}:
        return True
    return False

def sol(x):
    global sdk
    if x == len(loc):
        return

    for i in range(1,9):
        r,c = loc[x]
        sdk[r][c] = i
        if check(r,c):
            sol(x+1)

sol(0)
sdk       
# %%
check(0,0)
# %%
