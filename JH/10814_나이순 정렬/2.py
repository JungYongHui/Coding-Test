#%%
from sys import stdin
n = int(stdin.readline())

id_a = tuple(stdin.readline() for _ in range(n))
id_b = ((int(j.split()[0]),i) for i,j in enumerate(id_a))
id_c = (id_a[i[1]] for i in sorted(id_b))

print("".join(id_c))

# %%
