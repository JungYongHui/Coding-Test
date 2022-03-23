"""
1. 벽을 선택한다. -> 조합
2. 바이러스를 퍼트린다. -> bfs or dfs
3. 바이러스가 퍼지지 않은 안전지역 면적을 구한다.

1~3번의 과정을 벽을 선택하는 모든 경우의 수에 대해서 반복하고,
마지막에 안전지역의 MAX값을 리턴한다.
"""

import copy
import sys

# 지도 받기
input = sys.stdin.readline

N, M = map(int, input().split())
mapping = []
for _ in range(N):
    m = list(map(int, input().split()))
    mapping.append(m)


dr = [-1, 0, 1, 0] # 위아래 row 단위로 이동한다.
dc = [0, 1, 0, -1] # 좌우 column 단위로 이동한다.

max_value = 0 # clean 지역의 개수를 return하기 위한 변수

# 벽 선택하기
def select_wall(start, count):
    global max_value
    
    if count == 3: # 종료조건, 벽 3개 선택하기.
        # deepcopy : 깊은 복사(내부 객체들까지 복사한다.)
        sel_NM = copy.deepcopy(mapping) # deepcopy로 벽이 선택된 배열 복사
        for r in range(N):# 바이러스 퍼트리기
            for c in range(M): # 바이러스 퍼트리기
                spread_virus(r, c, sel_NM)
        safe_counts = sum(i.count(0) for i in sel_NM) # clean인 지역 count
        max_value = max(max_value, safe_counts)
        return True
    
    else:
        for i in range(start, N*M): # 2차원 배열에서 조합 구하기
            r = i // M
            c = i % M
            if mapping[r][c] == 0: # 안전영역인 경우 벽으로 선택한다.
                mapping[r][c] = 1 # 벽으로 변경한다.
                select_wall(i, count+1) # 벽 선택
                mapping[r][c] = 0
                
                
# 바이러스 퍼뜨리기
def spread_virus(r, c, sel_NM):
    if sel_NM[r][c] == 2:
        # 상하좌우 4방향을 확인하고 범위를 벗어나거나, 벽을 만날때까지 반복한다.
        for dir in range(4):
            n_r = r+dr[dir]
            n_c = c+dc[dir]
            
            if n_r >= 0 and n_c >=0 and n_r < N and n_c < M: # 범위를 벗어나지 않을 때
                if sel_NM[n_r][n_c] == 0:
                    sel_NM[n_r][n_c] = 2
                    spread_virus(n_r, n_c, sel_NM)

            