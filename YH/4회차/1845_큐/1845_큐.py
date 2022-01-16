import sys
from collections import deque

def push(x, queue):
    queue.append(x)
    return queue

def pop_q(queue):
    if len(queue) == 0:
        print(-1)
        return queue
    else:
        print(queue.popleft())
        return queue

def size(queue):
    print(len(queue))

def empty(queue):
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def back(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])

n = int(input())

queue = deque()

for i in range(n):
    func = sys.stdin.readline().rstrip()
    func_list = func.split()
    if func_list[0] == 'push':
        queue = push(int(func_list[1]), queue)
    elif func_list[0] == 'pop':
        queue = pop_q(queue)
    elif func_list[0] == 'size':
        size(queue)
    elif func_list[0] == 'empty':
        empty(queue)
    elif func_list[0] == 'front':
        front(queue)
    elif func_list[0] == 'back':
        back(queue)