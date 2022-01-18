## 100ms

import sys
from collections import deque

def push_front(x, queue):
    queue.appendleft(x)
    return queue

def push_back(x, queue):
    queue.append(x)
    return queue

def pop_front(queue):
    if len(queue) == 0:
        print(-1)
        return queue
    else:
        print(queue.popleft())
        return queue

def pop_back(queue):
    if len(queue) == 0:
        print(-1)
        return queue
    else:
        print(queue.pop())
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
    if func_list[0] == 'push_front':
        queue = push_front(int(func_list[1]), queue)
    elif func_list[0] == 'push_back':
        queue = push_back(int(func_list[1]), queue)
    elif func_list[0] == 'pop_front':
        queue = pop_front(queue)
    elif func_list[0] == 'pop_back':
        queue = pop_back(queue)
    elif func_list[0] == 'size':
        size(queue)
    elif func_list[0] == 'empty':
        empty(queue)
    elif func_list[0] == 'front':
        front(queue)
    elif func_list[0] == 'back':
        back(queue)