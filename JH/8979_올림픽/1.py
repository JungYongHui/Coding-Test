from sys import stdin
n,t = map(int,stdin.readline().split())
arr=[]
medals=[]
for _ in range(n):
    country, g, s, v = map(int,stdin.readline().split())
    medals.append((g, s, v))
    arr.append(country)
arr.sort(key=lambda x: medals[0])
print(arr)
#%%