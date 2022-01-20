#%%
from sys import stdin
n = int(stdin.readline())

ids = stdin.readlines()

lst=[]
for i,id in enumerate(ids):
    id = id.split()
    age, name = id[0], id[1]
    lst.append((age, i, name))

lst.sort(key= lambda x: (int(x[0]),x[1]))

for id in lst:
    print(id[0],id[2])    
# %%
