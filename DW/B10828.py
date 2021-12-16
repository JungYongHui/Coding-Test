# 백준 10828번

import sys

stack = [] # 값들을 저장할 스택 생성
def output(input): # 결과 출력 함수
    global stack # 함수 밖의 스택을 불러옴

    if input[0] == 'push':
        stack.append(input[1]) # input은 list의 split 형태로 받기 때문에 두 번째 자리 값을 저장
 
    else:
        if input[0] == 'pop':
            if stack:
                pop_ = stack.pop()
                return print(pop_) # 스택의 맨 끝의 값을 뺀 후 그 값을 출력
            else:
                return print(-1) # 없으면(스택이 비어있음) -1을 출력

        elif input[0] == 'size':
            return print(len(stack)) # 스택의 길이
        
        elif input[0] == 'empty':
            if len(stack) == 0:
                return print(1) # 스택의 길이가 0이면(비어있다는 뜻) 1을 출력
            else:
                return print(0) # 그렇지 않으면(스택 길이가 0이 아니면) 0을 출력
        
        elif input[0] == 'top':
            try:
                return print(stack[-1]) # 스택의 맨 마지막 값을 출력(맨 위에 있는거)
            except:
                return print(-1) # 만약 스택에 값이 없다면, 에러를 발생하기에 except로 처리

# main
n = int(sys.stdin.readline())
for _ in range(n):
    input = sys.stdin.readline().split()
    output(input)