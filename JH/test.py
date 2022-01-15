#%%
import pandas as pd

a = [
    [1,0,0,0],
    [1,0,0,1],
    [0,0,0,1],
    [0,0,1,0],
    ]

df = pd.DataFrame(a)
df
# %%
df[df==1].index
# %%
