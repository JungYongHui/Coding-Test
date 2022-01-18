import sys

def push(queue, x):
    queue.append(x)
    return queue

def pop(queue):
    if len(queue) != 0:
        pop_ = queue.pop(0)
        print(pop_)
    else:
        print(-1)

def size(queue):
    print(len(queue))

def empty(queue):
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front(queue):
    if len(queue) != 0:
        print(queue[0])
    else:
        print(-1)

def back(queue):
    if len(queue) != 0:
        print(queue[-1])
    else:
        print(-1)    


f_input = int(sys.stdin.readline())

function_mapping = {'push': push,
                    'pop': pop,
                    'size': size,
                    'empty': empty,
                    'front': front,
                    'back': back}

queue = []
for _ in range(f_input):
    s_input = sys.stdin.readline().split() # s_input[0], s_input[1]
    if s_input[0] == 'push':
        queue = function_mapping[s_input[0]](queue,s_input[1])
    else:
        function_mapping[s_input[0]](queue)