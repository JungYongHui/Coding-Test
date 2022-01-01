from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
for _ in range(n):
    I = input()
    len_lst = int(input())
    lst = input().lstrip('[').rstrip(']').split(',')

    r_flag = False
    r_del,l_del = 0, 0
    del_cnt = 0
    error = False

    for i in I:
        if i == 'R':
            r_flag = not r_flag
        elif i == 'D':
            if r_flag:
                r_del -= 1
            else:
                l_del += 1
            del_cnt +=1
        if del_cnt > len_lst:
            error = True
            break
    # print    
    if error:
        print('error')
    else:

        if r_del == 0:
            r_del = None
        if l_del == 0:
            l_del = None

        print('[',end='')
        if r_flag: 
            print(*reversed(lst[l_del:r_del]),sep=',',end='') 
        else:
            print(*lst[l_del:r_del],sep=',',end='') 
        print(']')