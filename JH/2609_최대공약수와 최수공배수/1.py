#%% math 라이브러리 사용
from math import gcd
a,b = map(int,input().split())
x=gcd(a,b)
print(f'{x}\n{a*b//x}')
#%%
a,b=map(int,input().split());l=a*b
while b:a,b=b,a%b
print(a,l//a)
# %%
