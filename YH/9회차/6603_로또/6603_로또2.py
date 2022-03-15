# 조합을 DFS로 구현

def dfs(idx, list):
    if len(list) == lim:
        print(*list, end=' ')
        print()
        return

    for i in range(idx, len(s)):
        dfs(i+1, list+[s[i]])

while True:
    inp = list(map(int, input().split()))
    k, s = inp[0], inp[1:]
    answer = []
    lim = 6

    if k == 0:
        break

    dfs(0, [])