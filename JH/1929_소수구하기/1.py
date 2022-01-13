m, n = map(int,input().split())

lst = [True] * (n+1)
i = 2
while i < (n+1):
    if lst[i]:
        if i >= m:
            print(i)
        j=i
        while True:
            try:
                lst[j] = False
                j+=i    
            except:
                break            
    i+=1