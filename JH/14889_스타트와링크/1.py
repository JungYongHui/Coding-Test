# %%
n=6

arr = [
    [0, 1, 2, 3, 4, 5],
    [1, 0, 2, 3, 4, 5],
    [1, 2, 0, 3, 4, 5],
    [1, 2, 3, 0, 4, 5],
    [1, 2, 3, 4, 0, 5],
    [1, 2, 3, 4, 5, 0],
    ]

#%%
from sys import stdin
# input = stdin.readline
n=int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]
arr = tuple(tuple(map(int,l.split())) for l in stdin.readlines())
print(arr)
#%%
visited = [0] * n
visited[0] =1

lst=[[0],{*range(1,n)}]
start,link=0,0

for i in arr[1:]:
    link += sum(i[1:])
    # print(i[1:])

ans=float('inf')

def dfs(idx, cnt, lst,start,link):
    global ans
    if cnt == n//2:
        # print(visited, lst)
        ans = min(ans,abs(start-link))
        # print(f'!!!!!!!!!!{ans=}')
        return

    for i in range(idx,n):
        visited[i] = 1
        start_, link_ = start, link
        for j in lst[0]:
            start += arr[i][j]
            start += arr[j][i]
        lst[0].append(i)
        lst[1].remove(i)
        for j in lst[1]:
                link -= arr[i][j]
                link -= arr[j][i]
        # print(visited, lst, start, link)
        dfs(i+1, cnt+1, lst, start, link)

        visited[i] = 0
        lst[1].add(lst[0].pop())
        start,link = start_,link_

dfs(1,1,lst,start,link)
print(ans)
# %%
