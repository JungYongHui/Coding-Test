#%% import
import sys
input =sys.stdin.readline
#%%
def push(queue, element):
    queue.append(element)
    return queue

def pop(queue):
    try:
        pop,*queue = queue
        print(pop)
    except ValueError:
        print(-1)
    finally:
        return queue

def size(queue):
    print(len(queue))
    return queue

def empty(queue):
    if queue:
        print(0)
    else:
        print(1)
    return queue

def front(queue):
    try:
        print(queue[0])
    except IndexError:
        print(-1)
    finally:
        return queue

def back(queue):
    try:
        print(queue[-1])
    except IndexError:
        print(-1)
    finally:
        return queue
#%%
func_mapping = {'push': push,
                'pop': pop,
                'size': size,
                'empty': empty,
                'front': front,
                'back': back,
                }
#%%
queue = []
for i in range(int(input())):
    func_name, *arg = input().split()
    queue =func_mapping[func_name](queue, *arg)
# %%