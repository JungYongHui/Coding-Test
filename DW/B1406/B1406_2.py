import sys
from collections import deque

# 커서 -> 인덱스
# 인덱스에 해당하는 숫자 -> 박스
# insert를 활용한다.

# 커서의 추가 -> index+1


def P(x):
    global index
    f_input.insert(index, x)
    index += 1

def L():
    global index # 어떤 연산이 이루어질 땐 전역변수를 사용해야한다?
    if index == 0: # 커서가 문장의 맨 앞이면 무시한다.
        return
    index -= 1 

def D():
    global index
    if index == len(f_input):
        return

    index += 1

def B():
    global index
    if index == 0:
        return
    
    elif index == len(f_input):
        del f_input[index-1]
        index -= 1
    
    else:
        del f_input[index-1]
        index -= 1


f_input = list(sys.stdin.readline().rstrip())
f_input = deque(f_input)
index = len(f_input) # 초기 시작 커서지점
num_input = int(sys.stdin.readline())


for _ in range(num_input):
    s_input = sys.stdin.readline().split()
    if len(s_input) == 2:
        P(s_input[1])
    else:
        if s_input[0] == 'L':
            L()
        elif s_input[0] == 'D':
            D()
        else: # s_input[0] == 'B':
            B()
    
answer = ''.join([str(_) for _ in f_input])
print('답:', answer)

