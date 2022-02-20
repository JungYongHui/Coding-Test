# import sys

# def DFS(start, depth): # 여기에서 start, depth를 주목!
#     if depth == 6:
#         for i in range(6):
#             print(combi[i], end = '')
#         print() # 다음 줄에 또 출력하기 위함
#         return # ** return이 되면 for문으로 넘어가게 됨.
    
#     for i in range(start, len(s)): # 여기에서 range가 포인트임. start를 주목!
#         ##### 여기 를 이해할 수 있어야함.####
#         combi[depth] = s[i]
#         DFS(i + 1, depth + 1)
#         ####################################
        
# combi = [0 for i in range(13)]
# while True:
#     s = list(map(int, input().split()))
#     if s[0] == 0:
#         break
#     # 작동 시작
#     del s[0]
#     DFS(0, 0)
#     print() # 다음 코드 입력받기

def DFS(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end = ' ')
        print() # 입력받은 상태에서 다음 로또 번호를 출력시키기.
        return
    
    for i in range(start, len(s)):
        combi[depth] = s[i]
        DFS(i+1, depth+1) # 한칸 씩 늘린다!


combi = [i for i in range(13)]
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    
    ### 알고리즘이 작동한다.
    del s[0] # 주어진 K값을 제거하고,
    DFS(0, 0)
    print() # 다음 입력을 받기 위해서 한칸 띄어주기

