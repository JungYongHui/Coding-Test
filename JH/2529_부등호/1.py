#%%
n = 9
operators = "> < < < > > > < <".split()
operators = [True if i == '<' else False\
    for i in operators]
operators
# %%
ans = [0]
i=0
while i <= n:
    if operators[i]:
        for j in range(0,ans[i]):
            if j not in ans[i]:
                ans.append(j)
                i+=1
                break
        else:
            ans.append(ans.pop())
    if operators[i]:
        for j in range(9,ans[i],-1):
            if j not in ans[i]:
                ans.append(j)
                i+=1
                break
        else:
            ans.append(ans.pop()+1)
#%%
print(*range(10,5,-1))
# %%
