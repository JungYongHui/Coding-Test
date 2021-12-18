from sys import stdin

def push(inp):
    stack.append(inp)
    return stack

def pop():
    if len(stack) != 0:
        print(stack[-1])
        del stack[-1]
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) != 0:
        print(stack[-1])
    else:
        print(-1)


stack = []

n = int(stdin.readline())

for i in range(n):
    inp_list = list(stdin.readline().split())
    if inp_list[0] == 'push':
        push(inp_list[1])
    elif inp_list[0] == 'pop':
        pop()
    elif inp_list[0] == 'size':
        size()
    elif inp_list[0] == 'empty':
        empty()
    elif inp_list[0] == 'top':
        top()