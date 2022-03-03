from collections import deque

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

r_plus = [-1, 0 ,1, 0]
c_plus = [0, -1, 0, 1]

def bfs(row, col):
    queue = deque()
    queue.append((row, col))

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            new_r = row + r_plus[i]
            new_c = col + c_plus[i]

            if new_r < 0 or new_r >= n or new_c < 0 or new_c >= m:
                continue
            if graph[new_r][new_c] == 0:
                continue
            if graph[new_r][new_c] == 1:
                graph[new_r][new_c] = graph[row][col] + 1
                queue.append((new_r, new_c))
    return graph[n-1][m-1]

print(bfs(0,0))
print(graph)