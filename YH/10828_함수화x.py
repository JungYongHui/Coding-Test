from sys import stdin

stack = []

n = int(stdin.readline())

for i in range(n):
    inp_list = list(stdin.readline().split())
    if inp_list[0] == 'push':
        stack.append(int(inp_list[1]))

    elif inp_list[0] == 'pop':
        if len(stack) != 0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)

    elif inp_list[0] == 'size':
        print(len(stack))

    elif inp_list[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif inp_list[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)