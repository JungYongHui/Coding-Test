## key point ##
## deque 사용과, reverse를 매 입력마다 실행이 아닌 특정 경우만 실행 ##

import sys
from collections import deque
# deque를 사용하는 이유 : popleft의 시간 차이
# list의 경우 pop()으로 마지막 값을 꺼내는 경우 O(1) 시간이 걸림,
# pop(0)로 가장 앞든을 꺼낼떄는 list 크기에 따라 읽어오는 시간이 달라짐 O(n)
# deque를 사용할 경우 popleft()를 사용하면 리스트의 O(1)의 시간이 걸림 => index의 주소 값으로 바로 값을 찾음

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip() # function input
    n = int(input()) # 배열의 개수 n
    arr = sys.stdin.readline().rstrip()[1:-1].split(",") # [a,b] 형태의 input을 list로 변환
    queue = deque(arr) # list를 deque로 변환

    rev = 0  # 총 reverse 가 몇번 입력됐는지 확인용 변수
    flag = 0  # arr의 길이가 0인지 확인하는 변수

    # 배열의 크기가 0일 경우
    if n == 0:
        queue = []

    for j in p:
        # R function이 입력될 경우
        if j == 'R':
            rev += 1 # rev 변수 +1
        # D function이 입력될 경우
        elif j == 'D':
            # queue 길이가 0일 경우 error 출력, flag = 1
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0: # rev 변수가 짝수 = queue 상태가 원상태
                    queue.popleft() # queue에서 popleft
                else: # rev 변수가 홀수 = queue가 reverse된 경우
                    queue.pop() # queue에서 pop : 맨 뒤의 요소를 pop

    if flag == 0: # queue 길이가 0이 아닌 경우
        if rev % 2 == 0: # rev가 짝수면 queue 그대로 출력
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse() # rev가 홀수이면 queue reverse 후 출력
            print("[" + ",".join(queue) + "]")