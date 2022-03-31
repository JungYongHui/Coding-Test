def dfs(x, y, count):
    xx, yy = [-1, 0, 1, 0], [0, -1, 0, 1]
    if graph[x][y] == 1:
        # if x and y == 0:
        #     count = 0
        count += 1
        graph[x][y] = count

        for i in range(4):
            new_x, new_y = x + xx[i], y + yy[i]
            if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
                dfs(new_x, new_y, count)
    return graph

count = 0
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

graph = dfs(0,0,count)
for row in graph:
    print(row)

