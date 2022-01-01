def push(x):
    stack.append(x)

def pop():
    print(stack.pop())

def size():
    print(len(stack))

def empty():
    print(int(not stack))

def top():
    try:
        print(stack[-1])
    except IndexError:
        print(-1)
#%%
def convert():
    func_name, *arg = input().split()
    vars()[func_name](*arg)
# %%
stack=[]
for _ in range(int(input())):
    func_name, *arg = input().split()
    vars()[func_name](*arg)
#%%
