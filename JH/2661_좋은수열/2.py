#%%
n=int(input())
arr=[0]*n
arr[0]=1

def foo(i,arr):
    j=0
    while i-1-2*j>=0:
        if arr[i-1-2*j:i-j] == arr[i-j:i+1]:
            return False
        j+=1
    return True

i=0
while True:
    if foo(i,arr):
        if i==n-1:
            break
        i+=1
        arr[i]+=1
    else:
        while True:
            if arr[i]<3:
                arr[i]+=1
                break
            else:
                arr[i]=0
                i-=1
print("".join(map(str,arr)))
# %%
