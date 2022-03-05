N, M = map(int, input().split())

maps = []
for _ in range(N):
    maps.append(list(map(int, input())))

def dfs(row, col):

    if row <= -1 or row >= N or col <= -1 or col >= M:
        return False

    if maps[row][col] == 0:
        maps[row][col] = 1
        dfs(row - 1, col)
        dfs(row, col - 1)
        dfs(row + 1, col)
        dfs(row, col + 1)
        return True

    return False

group = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            group += 1

print(group)