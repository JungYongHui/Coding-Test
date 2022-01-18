#%%
def append(element:int):
    i = len(heap)
    j = i//2
    heap.append(element)
    try:
        while heap[i]>heap[j]:
            heap[i],heap[j] = heap[j],heap[i]
            i,j = j,j//2
    except TypeError:
        pass
    # print(heap)

def pop():
    try:
        ans = 0
        heap[1],heap[-1] = heap[-1],heap[1]
        ans = heap.pop()
        i,j = 1,2
        while True:
            try:
                if heap[j] < heap[j+1]:
                    j += 1
            except:
                pass
            
            if heap[i] < heap[j]:
                heap[i],heap[j] = heap[j],heap[i]
            else:
                break
            i,j = j, 2*j
    except:
        pass
    return ans
    # print(heap,ans)
# %%
from sys import stdin
_ = input()

lst = map(int,stdin.readlines())

heap = [None]

for i in lst:
    if i:
        append(i)
        # print(f'append({i}): {heap}')
    else:
        print(pop())
        # print(f'pop():    {heap}')
        
# %%
