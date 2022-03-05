n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

def dfs(row, col, s):
    while s!=0:
        if row <= -1 or row >= n or col <= -1 or col >= n:
            return False

        for i in range(1, k+1):
            if graph[row][col] == i:
                if graph[row-1][col] == 0:
                    graph[row - 1][col] = i
                elif graph[row][col-1] == 0:
                    graph[row][col-1] = i
                elif graph[row+1][col] == 0:
                    graph[row+1][col] = i
                elif graph[row][col+1] == 0:
                    graph[row][col+1] = i
        dfs(row-1, col, s)
        dfs(row, col-1, s)
        dfs(row+1, col, s)
        dfs(row, col+1, s)
        s -= 1
        return True

for i in range(n):
    for j in range(n):
        if dfs(i, j, s) == True:
            print(graph[x-1][y-1])