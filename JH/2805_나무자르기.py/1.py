#%%
I1='4 7'
I2='20 15 10 17'
I1='5 20'
I2='4 42 40 26 46'
I1='1 1'
I2='1'
# I1=input()
# I2=input()

n, target = (int(i) for i in I1.split())
trees  = [int(i) for i in I2.split()]
# %%
l, r = 0, 1_000_000_000

while l<=r:
    mid = (l + r)//2
    
    sum = 0
    for tree in trees:
        if tree > mid:
            sum += tree-mid

    if sum >= target:
        l = mid + 1
    else:
        r = mid - 1
print(mid)
# %%
I2='1\n'
[int(i) for i in I2.split()]
