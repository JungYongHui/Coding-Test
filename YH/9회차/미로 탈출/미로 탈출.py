def dfs(x, y, old_x, old_y):
    xx, yy = [-1, 0, 1, 0], [0, -1, 0, 1]

    if graph[x][y] == 1:
        graph[x][y] = graph[old_x][old_y] + 1
        for i in range(4):
            new_x, new_y = x + xx[i], y + yy[i]
            if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
                dfs(new_x, new_y, x, y)
    return graph




n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

graph = dfs(0,0,0,0)
for row in graph:
    print(row)