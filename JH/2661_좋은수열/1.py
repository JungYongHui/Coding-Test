# %%
# N=int(input())
N=8
a=0
while N > 2**(a+1):
    a+=1
#%%
arr=['1','2','3']
for _ in range(2):
    arr_=[]
    cnt=0
    for i in arr:
        for j in arr:
            if (i[-1] != j[0]) and (i!=j):
                arr_.append(i+j)
                print(arr.index(i),arr.index(j))
                cnt+=1
    print('_____________')
        #     if cnt==3:
        #         break
        # if cnt==3:
        #     break
    arr=arr_
# for _ in range(3):
#     arr=[
#         arr[0]+arr[1],
#         arr[0]+arr[2],
#         arr[2]+arr[0],
#         ]
# arr
    # %%
if N == 2**(a+1):
    print(arr[0]+arr[1])
else:
    print((arr[0]*2)[:N])
# %%
