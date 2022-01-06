import sys

num1 = int(sys.stdin.readline())
arr1 = list(map(int, list(sys.stdin.readline().split())))
num2 = int(sys.stdin.readline())
arr2 = list(map(int, list(sys.stdin.readline().split())))

arr1.sort() # 오름차순 정렬

# 이분탐색 / 초기 인덱스 : 중앙지점

for arr2_num in arr2:
    arr_idx = int(num1/2)
    while True:
        if arr1[arr_idx] == arr2_num:
            print(1)
            break
        else:
            if len(arr1) == 1:
                print(0)
                break
            elif arr1[arr_idx] > arr2_num:
                arr1 = arr1[:arr_idx]
            else:
                arr1 = arr1[arr_idx:-1]