from sys import stdin
input = lambda: stdin.readline().rstrip()

n=int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

for i in range(n-1):
    r,g,b = lst[i+1]
    r_,g_,b_ = lst[i]
    lst[i+1] = [
        r+min(g_,b_),
        g+min(r_,b_),
        b+min(r_,g_)
        ]

# print(lst[-1])
print(min(lst[-1]))