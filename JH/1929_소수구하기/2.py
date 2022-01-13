#%%
m, n = map(int,input().split())
#%%
lst = [True] * (n+1)
lst[:2] = [False,False]

end = int(n**0.5)
i = 2

for i in range(2,end+1):
    if lst[i]:
        for j in range(2*i, n+1, i):
            lst[j] = False 

for i in range(m,n+1):
    if lst[i]:
        print(i)
# %%
