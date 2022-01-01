#%%
I1='4 7'
I2='20 15 10 17'
I1='5 20'
I2='4 42 40 26 46'
I1='1 1'
I2='1'
I1=input()
I2=input()

n, target = (int(i) for i in I1.split())
trees  = [int(i) for i in I2.split()]
# %%
def calc_get_tree(length, h):
    if (l:=length-h) > 0:
        return l
    else:
        return 0

def calc_get_all_trees(trees, h):
    func = lambda x: calc_get_tree(x,h)
    return sum(map(func, trees))

# calc_get_all_trees(trees, h)
# %%
b = 0
t = 1_000_000_000
h = 500_000_000

# cnt = 40
converge = h - t

while converge != 0:
    h_ = h

    if (e:= calc_get_all_trees(trees, h) - target) < 0:
        t = h
        q,r = divmod(b+t, 2)
        h = q
    else:
        b = h
        q,r = divmod(b+t, 2)
        h = q


    converge = h - h_

    #debug
    # print(b,h,t,converge)
    # cnt-=1
    # assert cnt>0

print(h)
#%%
# print(b,t)

# %%
