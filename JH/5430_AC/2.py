#%%
import sys
input = lambda: sys.stdin.readline().rstrip()
#%%
def process_commend(commend:str, size:int):
    r_flag = False
    d_r = 0
    d_l = 0
    for i in commend:
        if i == 'R':
            r_flag = not r_flag
        else:
            if size == 0:
                return False
            elif r_flag:
                d_r -= 1
            else:
                d_l += 1
            size -=1
    if r_flag:
        flow = -1
    else:
        flow = 1
    return flow, d_l, d_r

def print_arr(lst, flow, d_l, d_r):
    if d_r == 0:
        d_r = None
    if d_l == 0:
        d_l = None
    lst = lst[d_l:d_r]
    lst = lst[::flow]
    print('[',end='')
    print(*lst,sep=',',end='')
    print(']')

# %%
for _ in range(int(input())):
    try:
        flow, d_l, d_r = process_commend(input(), int(input()))
        lst = input().lstrip('[').rstrip(']').split(',')
        print_arr(lst, flow, d_l, d_r)
    except:
        lst = input()
        print('error')