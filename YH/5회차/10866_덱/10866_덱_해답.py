# 80ms
# key point: stack 2개를 이용하여 deque를 생성할 수 있다.
import sys

N = int(sys.stdin.readline())

stack_1 = []
stack_2 = []
for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    # front가 오면 stack_1에 저장
    # back이 나오면 stack_2에 저장
    if command[0] == 'push_front':
        stack_1.append(command[1])
    elif command[0] == 'push_back':
        stack_2.append(command[1])
    elif command[0] == 'pop_front':
        if stack_1:
            print(stack_1.pop())
        else:
            if stack_2:
                print(stack_2.pop(0))
            else:
                print(-1)
    elif command[0] == 'pop_back':
        if stack_2:
            print(stack_2.pop())
        else:
            if stack_1:
                print(stack_1.pop(0))
            else:
                print(-1)
    elif command[0] == 'size':
        print(len(stack_1)+len(stack_2))
    elif command[0] == 'empty':
        if stack_1 or stack_2:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if stack_1:
            print(stack_1[-1])
        else:
            if stack_2:
                print(stack_2[0])
            else:
                print(-1)
    elif command[0] == 'back':
        if stack_2:
            print(stack_2[-1])
        else:
            if stack_1:
                print(stack_1[0])
            else:
                print(-1)