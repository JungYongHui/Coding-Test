#%%
n = 4
requests = [120, 110,140, 150]
budget = 485

# n = 5
# requests = [70, 80, 30, 40,100]
# budget = 450

n = int(input())
requests = [int(i) for i in input().split()]
budget = int(input())



def foo(limit):
    return sum(min(limit,r) for r in requests)

l, r = 1, 100_000
if sum(requests) > budget:
    while l<=r:
        mid = (l+r)//2
        if foo(mid) <= budget:
            l = mid+1
        else:
            r = mid-1
        # print(l,mid,r)
    print(r)
else:
    print(max(requests))
# %%
