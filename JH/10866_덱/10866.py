#%% import
import sys
input =sys.stdin.readline
#%%
def push_front(deque:list, element):
    deque.insert(0,element)
    return deque

def push_back(deque:list, element):
    deque.append(element)
    return deque

def pop_front(deque:list):
    try:
        pop,*deque = deque
        print(pop)
    except ValueError:
        print(-1)
    finally:
        return deque

def pop_back(deque:list):
    try:
        *deque, pop = deque
        print(pop)
    except ValueError:
        print(-1)
    finally:
        return deque

def size(deque:list):
    print(len(deque))
    return deque

def empty(deque:list):
    if deque:
        print(0)
    else:
        print(1)
    return deque

def front(deque:list):
    try:
        print(deque[0])
    except IndexError:
        print(-1)
    finally:
        return deque

def back(deque:list):
    try:
        print(deque[-1])
    except IndexError:
        print(-1)
    finally:
        return deque
#%%
func_mapping = {'push_front': push_front,
                'push_back': push_back,
                'pop_front': pop_front,
                'pop_back': pop_back,
                'size': size,
                'empty': empty,
                'front': front,
                'back': back,
                }
#%%
deque = []
for i in range(int(input())):
    func_name, *arg = input().split()
    deque =func_mapping[func_name](deque, *arg)
# %%