from itertools import combinations #자동으로 사전 순으로 정렬
import sys

input=sys.stdin.readline
while 1:
    arr = input().split()
    if arr.pop(0) == '0':
        break
    for i in combinations(arr, 6):
        print(" ".join(i))
    print()


# import sys
# from itertools import permutations
# input = sys.stdin.readline
#
# while True:
#     arr = list(map(int, input().split()))
#     n = arr.pop(0)
#     arr_p = list(permutations(arr, 6))
#     # permutation의 시간복잡도 O(n!) 아슬아슬하게 통과
#     for case in arr_p:
#         case = list(case)
#         if case != sorted(case):
#             continue
#         elif case == sorted(case):
#             print(*case)
#             continue
#     print()
#     if n == 0:
#         break