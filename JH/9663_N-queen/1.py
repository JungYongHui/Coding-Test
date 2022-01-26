#%%
n=10
# n= int(input())
# n=5
board=[None]*n # board[i] 이면 (i,board[i])위치에 말이 있음
def sol(x):
    # print(f'sol({x}) {board}')
    # n개의 퀸이 배치되어있다면 이경우가 답
    if x == n:
        sol.ans += 1
        return

    for y in range(n):
        flag = True
        for x_ in range(x):
            if (abs(x-x_) == abs(y-board[x_]) or y==board[x_]):
                flag = False
                break
        if flag:
            board[x]=y
            # print(board)
            sol(x+1)
    
sol.ans=0
sol(0)
print(sol.ans)
# %%
def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[i]-col[x]) == x-i:
            return False
    return True

def dfs(x):
    global res
    if x == n:
        res += 1
        return
    for i in range(n):
        col[x] = i
        if check(x):
            dfs(x+1)

# n = int(input())
res = 0
col = [0]*15
dfs(0)
print(res)
# %% 얘만 통과 하네???
def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True
        
        
#한줄씩 재귀하며 DFS를 실행
def dfs(x):
    global result
    
    if x == n:
        result += 1

    else:
        for i in range(n):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)

# n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)
# %%
