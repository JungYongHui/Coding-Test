#%%
I = int(input())
n=I
len_ = int(n**0.5)
#%%
arr=[1,0]*(n//2+1)
arr[:2]=[0,1]
prime=[2]
# arr
# %%
for idx in range(2,len_):
    if arr[idx]:
        prime.append(idx+1)
        # print(f"prime.append({idx+1})")
        for j in range(2*idx+1,n,idx+1):
            arr[j]=0

for idx in range(max(2,len_),n):
    if arr[idx]:
        prime.append(idx+1)
        # print(f"prime.append({idx+1})")
# prime
# %%
res=0
t = I
sum = 0
i,j=0,0
for idx in range(len(prime)):
    sum += prime[idx]
    # print(f'{sum=}   {prime[idx]} 추가')
    if sum>t:
        while sum > t:
            sum -= prime[j]
            # print(f'{sum=}   {prime[j]} 제거')
            j+=1
        if sum==t:
            res+=1
            # print(f"{sum=}!!!!!!!!!!")
    elif sum == t:
        res+=1
        # print(f"{sum=}!!!!!!!!!!")
print(res)
# %%