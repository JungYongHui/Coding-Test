from sys import stdin
n,t = map(int,stdin.readline().split())
country=[]
medals=[]
for _ in range(n):
    country_, g_, s_, b_ = map(int,stdin.readline().split())
    medals.append((g_, s_, b_))
    country.append(country_)

g,s,b = medals[country.index(t)]
cnt=0

for g_,s_,b_ in medals:
    if g_>g:
        cnt+=1
    elif g_ == g:
        if s_>s:
            cnt+=1
        elif s_ == s:
            if b_ > b:
                cnt+=1

print(cnt+1)
#%%
class cnt():
    ans=0
    def f(self):
        self.ans += 1

a = cnt()


def foo():
    a.f()
    a.f()
foo()
a.ans
# %%
