#%%
n= int(input())
board=[None]*n # board[i] 이면 (i,board[i])위치에 말이 있음
def sol(x):
    # print(f'sol({x})')
    # n개의 퀸이 배치되어있다면 이경우가 답
    if x == n:
        sol.ans += 1
        return

    for y in range(n):
        flag = True
        for x_ in range(x):
            if any((abs(x-x_) == abs(y-board[x_]), y==board[x_])):
                flag = False
        if flag:
            board[x]=y
            # print(board)
            sol(x+1)
    
sol.ans=0
sol(0)
print(sol.ans)
# %%
