#%%
import sys
input = sys.stdin.readline

#%%
def processing(file_length, file_num, file_importance_list):

    lst = file_importance_list
    sorted_lst = sorted(file_importance_list)
    seq = 1
    order = 0

    while True:

        if lst[order] == sorted_lst[-1]:

            if order-file_num:
                seq += 1
                sorted_lst.pop()

            else:
                print(seq)
                break

        order = (order+1)%file_length

#%%
for _ in range(int(input())):
    file_length, file_num = map(int, input().split())
    file_importance_list = list(map(int, input().split()))
    processing(file_length, file_num, file_importance_list)

#%%
