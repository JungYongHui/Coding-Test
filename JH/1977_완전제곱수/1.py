if (root_m := int(input())**0.5)%1 == 0:
    a = int(root_m)
else:
    a = int(root_m)+1
b = int(int(input())**0.5)

if a<=b:
    print(sum(map(lambda x:x**2,range(a,b+1))),a**2)
else:
    print(-1)
#%%