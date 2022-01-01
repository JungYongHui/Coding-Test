# %%
for _ in range(int(input())):
    C=input()
    l,r,d = 1,2*int(input()),1
    L=input()
    # print('['+lst[a:b:c]+']')
    for i in C:
        l,r,d=[(l+2*d,r,d),(r-d,l-d,-d)][i=='R']
        # ans = f'[{lst[a:b:c]}]'
        # print(f'[{L[l:r:d]}]')
    print([f'[{L[l:r:d]}]',['error','[]'][l-r==d]][l*d>r*d])
    # print(l,r)
