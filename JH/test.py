str_ = input()
l,r = 0,len(str_)-1
ans=1
while l<r:
    if str_[l] != str_[r]:
        ans = 0
        break

print(ans)