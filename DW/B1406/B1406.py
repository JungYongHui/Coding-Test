'''
<풀이 방법>
힌트 : 리스트를 2개 생성하여 마지막에 이어붙이기.

[a, b, c, d] []
[a, b, c, d, e] []
[a, b, c, d] [e] # pop, append # 이동했을 때
[a, b, c] [e, d] # pop, append
[a, b, c, x] [e, d] # 중간에 추가했을 때
[a, b, c] [e, d] # 중간에 삭제했을 때
[] [e, d, c, b, a] # 맨 오른쪽으로 이동 # 비어있으면, 아무런 변화x
'''

import sys

f_input = list(sys.stdin.readline().rstrip())
s_input = int(sys.stdin.readline())

a_box = f_input
b_box = []
for _ in range(s_input):
    t_input = sys.stdin.readline().split()
    try:
        if t_input[0] == 'P':
            a_box.append(t_input[1])
        elif t_input[0] == 'L':
            b_box.append(a_box.pop())
        elif t_input[0] == 'D':
            a_box.append(b_box.pop())
        else:
            a_box.pop()
    except:
        pass
print(''.join(a_box)+''.join(list(reversed(b_box))))
        
    
