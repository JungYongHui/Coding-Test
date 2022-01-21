#%%
from sys import stdin

def lcm(a,b):
    mul = a*b
    if b > a:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return mul//a

for _ in range(int(input())):
    a,b = map(int,stdin.readline().split())
    print(a,b)
    print(lcm(a,b))

# (str(lcm(map(int,i.split()))) for i in stdin.readlines())
# a=input()
# print("/n".join(str(lcm(map(int,i.split()))) for i in stdin.readlines()))

# %%
