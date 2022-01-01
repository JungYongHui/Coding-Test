#%%
from sys import stdin
input = stdin.readline

def foo(n):
    try:
        return foo.memo[n]

    except KeyError:
        ans = tuple(i+j for i,j in zip(foo(n-1),foo(n-2)))
        foo.memo[n] = ans
        return ans

    except AttributeError:
        foo.memo = {0:(1,0), 1:(0,1)}
        return foo(n)

N = int(input())

for _ in range(N):
    print(*foo(int(input())))
