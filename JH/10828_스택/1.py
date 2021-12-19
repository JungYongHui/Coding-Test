#%%
import sys

input = sys.stdin.readline

#%%
stack = []

def push(n):
    n = int(n)
    stack.append(n)

def pop():
    try:
        print(stack.pop())
    except:
        print(-1)

def size():
    print(len(stack))

def empty():
    if not stack:
        print(1)
    else:
        print(0)

def top():
    try:
        print(stack[-1])
    except:
        print(-1)

func_list = {
    'push': push,
    'pop': pop,
    'size': size,
    'empty': empty,
    'top': top,
    }

#%%
for i in range(int(input())):
    func_name, *arg = input().split()
    func_list[func_name](*arg)
# %%