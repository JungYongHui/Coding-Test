# %% main
from collections import deque
from sys import stdin

n_max = int(input())
start, end = map(int,input().split())
n_line = int(input())
lines = stdin.readlines()
link = {}
for str_ in lines:
    a,b = map(int,str_.split())
    a,b = a,b
    if link.get(a):
        link[a].append(b)
    else:
        link[a]=[b]
    if link.get(b):
        link[b].append(a)
    else:
        link[b]=[a]

ans={end:-1}
visited = deque([start])
ans[start] = 0
while visited:
    tmp = visited.popleft()
    if tmp == end:
        break
    for i in link[tmp]:
        link[i].remove(tmp)
        visited.append(i)
        ans[i] = ans[tmp]+1
print(ans[end])
# %%