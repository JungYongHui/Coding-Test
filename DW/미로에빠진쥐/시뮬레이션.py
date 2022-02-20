import os
import time

def DrawMaze(maze):
    os.system('cls')
    for y in range(0, len(maze)):
        for x in range(0, len(maze[0])):
            if(maze[y][x]==-1):
                print('ㅁ', end='')
            elif(maze[y][x]==0):
                print("%2s"%" ",end='')
            else:
                print("%2d"%(maze[y][x]),end='')
        print()
    time.sleep(0.5)
    
    
dx=[ 0,1,0,-1]
dy=[-1,0,1,0]
def GoRobotMouse(maze,sx,sy,foots):        
    DrawMaze(maze)        
    foot = maze[sy][sx]    
    for di in range(0,4):
       x = sx + dx[di]
       y = sy + dy[di]
       if(maze[y][x]==-2):
           maze[y][x]=foot+1
           foots.append([x,y])
           return True
       if(maze[y][x]==0):
           maze[y][x] = foot+1
           if(GoRobotMouse(maze,x,y,foots)):
               foots.append([x,y])
               return True
    return False
def FindLoad(maze,sx,sy):
    DrawMaze(maze)    
    foots=[]    
    GoRobotMouse(maze,sx,sy,foots)    
    DrawMaze(maze)
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
print(FindLoad(maze,1,1))