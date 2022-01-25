import sys
from collections import deque 

# 오른쪽 입력 .append
# 왼쪽 입력 .appendleft
# 오른쪽에서 삭제 .pop
# 왼쪽에서 삭제 .popleft


def push_front(deq, x):
    deq.appendleft(x)
    return deq

def push_back(deq, x):
    deq.append(x)
    return deq

def pop_front(deq):
    if len(deq) != 0:
        pop_ = deq.popleft()
        print(pop_)
    else:
        print(-1)

def pop_back(deq):
    if len(deq) != 0:
        pop_ = deq.pop()
        print(pop_)
    else:
        print(-1)

def size(deq):
    print(len(deq))

def empty(deq):
    if len(deq) == 0:
        print(1)
    else:
        print(0)

def front(deq):
    if len(deq) != 0:
        print(deq[0])
    else:
        print(-1)

def back(deq):
    if len(deq) != 0:
        print(deq[-1])
    else:
        print(-1)

func = {'push_front':push_front,
        'push_back':push_back ,
        'pop_front':pop_front,
        'pop_back':pop_back,
        'size':size,
        'empty':empty,
        'front':front,
        'back':back}
deq = deque()


f_input = int(sys.stdin.readline())
for _ in range(f_input):
    s_input = sys.stdin.readline().split()
    if 'push' in s_input[0]:
        deq = func[s_input[0]](deq, int(s_input[1]))
    else:
        func[s_input[0]](deq)

