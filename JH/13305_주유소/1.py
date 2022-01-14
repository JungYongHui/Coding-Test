#%%
n=4
roads = list(map(int,"2 3 1".split()))
fair = list(map(int,"5 2 4 1".split()))

roads = list(map(int,"3 3 4".split()))
fair = list(map(int,"1 1 1 1".split()))

n = input()
roads = list(map(int,input().split()))
fair = list(map(int,input().split()))

m = fair[0]
ans = 0

for r, f in zip(roads, fair):
    if m > f:
        m = f
    ans += m*r

print(ans)
# %%