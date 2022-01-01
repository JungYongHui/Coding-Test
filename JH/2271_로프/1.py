import sys

n = int(input())
lst = [int(sys.stdin.readline()) for _ in range(n)]
lst.sort(reverse=True)


w_lst = [i*a for i, a in enumerate(lst,1)]
print(max(w_lst))
