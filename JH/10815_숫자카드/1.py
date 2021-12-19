#%% input
'''
5                   => 상근이가 가지고 있는 숫자 카드의 개수 N
6 3 2 10 -10        => 숫자 카드에 적혀있는 정수
8                   => M(1 ≤ M ≤ 500,000)
10 9 -5 2 3 4 5 -10 => 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수
'''
#%%
#%%
input1 = input()
input2 = input()
input3 = input()
input4 = input()
#%%
n=int(input1)
n_list = sorted(set(int(i) for i in input2.split()))

m= int(input3) 
m_list = [(int(j),i) for i,j in enumerate(input4.split())]
m_list.sort()
# %%
lst = [0] * m
i,j = 0,0
while j < m:
    try:
        m_j = m_list[j][0]
        while m_j > (n_i := n_list[i]) :
            i += 1
        if m_j == n_i:
            lst[m_list[j][1]] = 1
        else:
            lst[m_list[j][1]] = 0
        j += 1
    except:
        break

print(*lst)
# %%
