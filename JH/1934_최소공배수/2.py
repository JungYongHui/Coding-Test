#%%
from sys import stdin

def lcm(a,b):
    mul = a*b
    if b > a:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return mul//a

print("\n".join(str(lcm(*map(int,stdin.readline().split()))) for _ in range(int(input()))))
