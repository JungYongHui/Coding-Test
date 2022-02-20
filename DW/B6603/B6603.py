import sys

input = sys.stdin.readline

def DFS(depth, start):
    if depth == 0:
        print(*out)
        return
    
    for i in range(start, K):
        out.append(arr[i])
        DFS(depth+1, i+1)
        out.pop()
        

out = []
while True:
    arr = input().split()
    K = arr.pop(0)
    print(arr)
    print(K)
    DFS(0, 0)
    print()
    if arr[0] == 0:
        break
        
    
