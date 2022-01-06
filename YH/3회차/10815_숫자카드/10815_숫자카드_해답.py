##############################################################################################
# Solution 1 (SET를 이용한 풀이)
##############################################################################################
input()
n = set(map(int, input().split()))
# print(n)
input()
m = list(map(int, input().split()))
for i in m:
    if i in n:
        print(1, end=' ')
    else:
        print(0, end=' ')

##############################################################################################
# Solution 2 (이진 탐색을 이용한 풀이)
##############################################################################################
n = int(input())
a = list(map(int, input().split()))
a.sort()

def binary_search(num):
    l = 0
    r = n-1
    while l <= r :
        mid = (l+r)//2
        if a[mid] == num :
            return 1
        elif a[mid] > num :
            r = mid - 1
            # 반 줄여주기 1
        else:
            l = mid + 1
            # 반 줄여주기 2
    return 0

input()
for num in list(map(int, input().split())):
    print(binary_search(num), end = ' ')