# Solution

# 동서남북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def GoRobotMouse(maze, sx, sy, foots):
    foot = maze[sx][sy] # 현위치
    
    # 동서남북으로 이동
    for di in range(0, 4):
        x = sx + dx[di]
        y = sy + dy[di]
        
        if(maze[x][y] == -2):
            maze[x][y] = foot + 1
            foots.append([x,y])
            return True
        if(maze[x][y] == 0):
            maze[x][y] = foot + 1
            
            # foots.append([x, y])
            # GoRobotMouse(maze, x, y, foots)
            if(GoRobotMouse(maze, x, y, foots)): # 맞은 길에 대해서만 발자취를 담아야 하기 때문임.
                foots.append([x, y])
                return True
    return False

def FindLoad(maze, sx, sy):
    foots = []
    GoRobotMouse(maze, sx, sy, foots)
    foots.reverse()
    return foots

maze = [
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1, 1, 0, 0, 0, 0,-1, 0, 0, 0, 0,-1],
    [-1, 0,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1,-1, 0,-1, 0, 0, 0,-1, 0,-1],
    [-1, 0,-1, 0, 0, 0, 0,-1,-1, 0, 0,-1],
    [-1, 0,-1, 0,-1,-1, 0,-1, 0,-1,-1,-1],
    [-1, 0,-1,-1, 0,-1, 0, 0, 0, 0, 0,-1],
    [-1, 0,-1, 0, 0,-1, 0,-1, 0,-1, 0,-1],
    [-1, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1,-1,-1, 0, 0,-1, 0, 0, 0,-1],
    [-1, 0, 0, 0,-1,-1,-1, 0, 0,-1,-2,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        ]

print(FindLoad(maze, 1, 1))