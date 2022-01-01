import sys
input=sys.stdin.readline

lst=[0]*10001

n=int(input())
for _ in range(n):
    i=int(input())
    lst[i] +=1
for i in range(10001):
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i)