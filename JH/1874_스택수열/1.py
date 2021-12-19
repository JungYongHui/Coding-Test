#%%
import sys
input = lambda: int(sys.stdin.readline().rstrip())

#%%
stack=[]
max_num = input()
num = 0
old_num = 1
temp_num = input()
flag = True
ans=''
while flag:
    try:
        num = temp_num
        stack.extend(range(old_num,num))
        ans += '+'*(num-old_num) + '+-'
        old_num = num + 1
        while (temp_num := input()) < num:
            ans += '-'
            if stack.pop() == temp_num:
                continue
            else:
                flag = False
                break

    except:
        break
if flag == True:
    print('\n'.join(ans))
else:
    print('NO')    
