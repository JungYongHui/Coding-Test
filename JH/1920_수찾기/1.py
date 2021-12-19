#%%
input1 = '5'
input2 = '4 1 5 2 3'
input2 = '4 1 5 2 3 1 2 3 4 5 9 8 7 4 98 3'
input3 = '5'
input4 = '1 3 7 9 5'
n_list = set(int(i) for i in input2.split())
sorted(n_list)
#%%
n=int(input1)
n_list = list(set(int(i) for i in input2.split()))

m= int(input3) 
m_list = [(int(j),i) for i,j in enumerate(input4.split())]
# %%
m_list.sort()

# %%
lst = [False] * m
i,j = 0,0
while j < m:
    try:
        m_j = m_list[j][0]
        while m_j > (n_i := n_list[i]) :
            i += 1
        if m_j == n_i:
            lst[m_list[j][1]] = True
        else:
            lst[m_list[j][1]] = False
        j += 1
    except:
        break

for i in lst:
    print(int(i))
#%%