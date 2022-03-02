import sys

graph = []

f_input = int(sys.stdin.readline())
for _ in range(f_input):
    s_input = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(s_input)

# graph = [[0,1,1,0,1,0,0],
#         [0,1,1,0,1,0,1],
#         [1,1,1,0,1,0,1],
#         [0,0,0,0,1,1,1],
#         [0,1,0,0,0,0,0],
#         [0,1,1,1,1,1,0],
#         [0,1,1,1,0,0,0]]

def DFS(graph,sx, sy):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    if sx<0 or sx>=f_input or sy<0 or sy>=f_input:
        return False
    
    if graph[sx][sy] == 1:
        global count
        count += 1 # 1을 찾았을 땐 카운팅을 해준다.
        graph[sx][sy] = 0 # 간 곳은 가지 않도록 0으로 처리
        
        for i in range(4):
            x = sx + dx[i]
            y = sy + dy[i]
            DFS(graph,x, y)
        return True
    return False


remember = [] # 단지 수 저장
count = 0 # 단지안에 있는 1 카운팅
result = 0 # 단지 자체에 대한 카운팅

for i in range(f_input):
    for j in range(f_input):
        if DFS(graph, i, j): # 이게 반환될 시점에 count가 되어있고, 1로 묶인 단지는 다 돌았을 것이다.
            remember.append(count)
            result += 1
            count = 0 # 다른 단지에 count를 해줘야하기 때문에

print(result)
remember.sort()
for i in remember:
    print(i)

            
            
