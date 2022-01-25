#%%
hq = [0]

def cond(i,j):
    return hq[i] > hq[j]

def push(a):
    hq.append(a)

    j = len(hq)-1
    i=j//2

    while i:
        if cond(j,i):
            hq[j], hq[i] = hq[i], hq[j]
            j,i = i,i//2
        else:
            break

def pop():
    
    hq[1], hq[-1] = hq[-1], hq[1]
    poped = hq.pop()
    
    i = 1
    while True:
        len_ = len(hq)-1
        j = 2*i
        if j > len_:
            break
        if j < len_:
            # if hq[j]<hq[j+1]:
            if cond(j+1,j):
                j+=1

        # if hq[j]<hq[j+1]:
        if cond(j,i):
            hq[j], hq[i] = hq[i], hq[j]
            i=j
        else:
            break
    return poped



from sys import stdin
n = int(input())

ans=[]
for _ in range(n):
    if (a:=int(stdin.readline())):
        push(a)
    else:
        if len(hq)-1:
            ans.append(pop())
        else:
            ans.append(0)

print(*ans,sep='\n')
# %%