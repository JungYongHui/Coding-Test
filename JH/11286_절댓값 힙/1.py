#%%
class heapq():
    def __init__(self) -> None:
        self.hq = [0]

    def cond(self,i,j):
        a,b = self.hq[i], self.hq[j]
        if abs(a) < abs(b):
            return True
        elif a == -b:
            return a<b
        else:
            return False

    def push(self,a):
        hq = self.hq
        hq.append(a)

        j = len(hq)-1
        i=j//2

        while i:
            # if hq[j] < hq[i]:
            if self.cond(j,i):
                hq[j], hq[i] = hq[i], hq[j]
                j,i = i,i//2
            else:
                break
    
    def pop(self):
        hq = self.hq
        
        hq[1], hq[-1] = hq[-1], hq[1]
        poped = hq.pop()
        
        i = 1
        while True:
            len_ = len(hq)-1
            j = 2*i
            if j > len_:
                break

            if j < len_:
                if self.cond(j+1,j):
                    j+=1

            if self.cond(j,i):
                hq[j], hq[i] = hq[i], hq[j]
                i=j
            else:
                break
        return poped

    def __len__(self):
        return(len(self.hq)-1)

from sys import stdin
n = int(input())

hq=heapq()
ans=[]
for _ in range(n):
    if (a:=int(stdin.readline())):
        hq.push(a)
    else:
        if len(hq):
            ans.append(hq.pop())
        else:
            ans.append(0)

print("\n".join(map(str,ans)))
# %%