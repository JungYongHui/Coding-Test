#%% https://www.acmicpc.net/problem/9012
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    str_=input().rstrip()    
    flag=True
    a=0
    for i in range(len(str_)):
        if str_[i] == "(":
            a+=1
        elif str_[i]==")":
            a-=1
        if a <0:
            flag=False

    if a!=0:
        flag=False

    print(["NO","YES"][flag])