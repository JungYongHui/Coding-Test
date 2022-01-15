#%%
# lst = list(map(int,"10 -4 3 1 5 6 -35 12 21 -1".split()))
# lst = list(map(int,"2 1 -4 3 4 -4 6 5 -5 1".split()))
# lst = list(map(int,"-1 -2 -3 -4 -5".split()))
n = input()
lst =list(map(int,input().split()))
# %%
l=[]
tmp=0
for i in lst:
    if 0 <= i*tmp:
        tmp += i
    else:
        l.append(tmp)
        tmp = i
l.append(tmp)

# %%
if len(l) == 1:
    if l[0] <= 0:
        print(max(lst))
        quit()

ans = tmp = 0
for i in l:
    if i > 0:
        tmp += i 
        ans = max(ans,tmp)
    else:
        tmp = max(0,tmp+i)
    # print(ans,tmp)
print(max(ans,tmp))
#%%
