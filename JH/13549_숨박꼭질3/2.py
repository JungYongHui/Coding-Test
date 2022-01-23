# 우선순위 큐 안쓰고 재귀로 풀기(참고함)
N,K=map(int,input().split())
def s(n,k):
    if n>=k:
        return n-k
    elif n==0:
        return 1+ s(1,k)
    elif k%2==0:
        return min(k-n,s(n,k//2))
    else:
        return 1 + min(s(n,(k-1)),s(n,(k+1)))
        
print(s(N,K))
    