import sys

n = int(input())
a_list = list(map(int, sys.stdin.readline().rstrip().split()))
a_list = list(set(a_list))
a_list.sort()

m = int(input())
b_list = list(map(int, sys.stdin.readline().rstrip().split()))

low, mid, high = 0, int(len(a_list)/2), len(a_list)-1

def bi_find(a_list, target, low, high):

    while low <= high:
        mid = (low + high)//2

        if a_list[mid] == target:
            return mid
        elif a_list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

for t in b_list:
    if bi_find(a_list, t, low, high) != -1:
        print(1, end=' ')
    else:
        print(0, end=' ')


