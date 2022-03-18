from collections import deque

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
count = 0

def bfs(x, y):
    deq = deque()
    deq.append((x, y))
    graph[x][y] = 1

    while deq:
        result = 0
        x, y = deq.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
                if graph[new_x][new_y] == 0:
                    graph[new_x][new_y] = 1
                    [print(row) for row in graph]
                    print()
                    deq.append((new_x, new_y))
                    result = 1
                    return result

    return result

for i in range(n):
    for j in range(m):
        result = bfs(i, j)
        print('result: ',result)
        count = count + result
        print('count: ', count)

print(count)


