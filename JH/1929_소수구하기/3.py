#%%
m, n = map(int,input().split())
lst = [False, False, *range(2,n+1)]
for i in lst:
    if i:
        if i <=  n**0.5:
            lst[2*i::i] =  ((n-i)//i) * [False]
    if m <= i <= n:
        print(i)

#%%
m, n = map(int, input().split())

def foo(m,n):
    lst = [True]*(n+1)
    lst[:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if lst[i]:
            lst[2*i::i] =  ((n-i)//i) * [False]
    
    for i in range(m, n+1):
        if lst[i]:
            print(i)

foo(m,n)
# %%
def foo(m,n):
    lst = [True]*(n+1)
    lst[:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if lst[i]:
            lst[2*i::i] =  ((n-i)//i) * [False]
    
    # print(*[i for i in range(m, n+1) if lst[i]],sep='\n')
    print('\n'.join(f'{i}' for i in range(m, n+1) if lst[i]))


foo(*map(int, input().split()))
# %%
m,n = map(int, input().split())
lst = [True]*(n+1)
lst[:2] = [False, False]

def foo(i):
    lst[2*i::i] =  ((n-i)//i) * [False]
    return i

a = [foo(i) for i in range(2, m) if lst[i]]
b = [f'{foo(i)}' for i in range(m, int(n**0.5)+1) if lst[i]]
c = [f'{i}' for i in range(int(n**0.5)+1,n+1) if lst[i]]

print('strat')
# print("\n".join((*b,*c)))
print('\n'.join([]))
print('end')
# %%
[2]+[3]
# %%
