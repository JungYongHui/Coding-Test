#%%
import sys
input = sys.stdin.readline

#%%
class Stack:
    def __init__(self):
        self.stack = []
        self.func_list = {
            'push': Stack.push,
            'pop': Stack.pop,
            'size': Stack.size,
            'empty': Stack.empty,
            'top': Stack.top,
            }

    def push(self, n):
        n = int(n)
        self.stack.append(n)

    def pop(self):
        try:
            print(self.stack.pop())
        except:
            print(-1)

    def size(self):
        print(len(self.stack))

    def empty(self):
        if not self.stack:
            print(1)
        else:
            print(0)

    def top(self):
        try:
            print(self.stack[-1])
        except:
            print(-1)

    def str_to_func(self, string):
        func_name, *arg = string.split()
        self.func_list[func_name](self,*arg)

#%%
stack = Stack()
for i in range(int(input())):
    stack.str_to_func(input())
# %%
# stack.push1(3)
# stack.str_to_func('push 1')
# stack.str_to_func('top')
# print(stack.stack)