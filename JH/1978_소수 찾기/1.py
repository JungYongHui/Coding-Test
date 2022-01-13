#%%
lst = [True]*1001
check = set()
i = 2
while i<1001:
    if lst[i]:
        check.add(i)
        j=i
        while True:
            try:
                lst[j] = False
                j+=i    
            except:
                break            
    i+=1

n = input()
nums = map(int, input().split())

r = 0 
for num in nums:
    if num in check:
        r +=1

print(r)

# %%
