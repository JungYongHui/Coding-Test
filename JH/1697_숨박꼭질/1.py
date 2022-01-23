#%%
from collections import deque

def solution(n,k):
    len_ = (max(n,2*k,100000)+1)
    lst = [-1] * len_

    queue_ = deque()

    queue_.append(n)
    lst[n] = 0
    flag = True

    while True:
        tmp = queue_.popleft()

        for next in (tmp-1, tmp+1, tmp*2):
            
            if (0<=next<len_):
                if (lst[next] == -1):
                    queue_.append(next)
                    lst[next] = lst[tmp]+1
                    # print(f'{lst[next]}:    {tmp} -> {next}')

            if next == k:
                return lst[k]

ans = solution(*map(int,input().split()))
print(ans)


# %%
