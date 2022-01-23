#%%
import heapq

def solution(n,k):
    lst = [-1] * (100001)

    queue_ = []

    lst[n] = 0
    heapq.heappush(queue_,(lst[n],n))

    while True:
        tmp = heapq.heappop(queue_)[1]

        for next in (tmp*2,):
            
            if (0<=next<100001):
                if (lst[next] == -1):
                    lst[next] = lst[tmp]
                    heapq.heappush(queue_,(lst[next],next))

            if next == k:
                return lst[k]

        for next in (tmp-1, tmp+1):
            
            if (0<=next<100001):
                if (lst[next] == -1):
                    lst[next] = lst[tmp]+1
                    heapq.heappush(queue_,(lst[next],next))
                if next == k:
                    return lst[k]


ans = solution(*map(int,input().split()))
print(ans)
# solution(5,17)
#%%
# %%
