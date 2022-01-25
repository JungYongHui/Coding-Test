import sys

# 퀵정렬
# 참고자료 폴더에 퀵정렬.py 참고할 것.
def new_sort(array, start, end):
    if start >= end:
        return
    # 야는 인덱스임, 헷갈리면 안됨.
    pivot = start
    left = start+1
    right = end

    while(left<=right):
        while(left<=end and array[pivot][1]>=array[left][1]):
            left+=1
        while(right>start and array[pivot][1]<=array[right][1]):
            right-=1
        if(left>right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    # 파티션 발동!
    new_sort(array, start, right-1)
    new_sort(array, right+1, end)

f_input = int(sys.stdin.readline())
array = []
for _ in range(f_input):
    s_input = tuple(map(int, sys.stdin.readline().split()))
    array.append(s_input)

# y값 증가순으로 정렬
new_sort(array, 0, len(array)-1)
# x값 증가순으로 정렬
for idx in range(len(array)):
    if idx==0:
        pass
    if array[idx-1][1] == array[idx][1]:
        if array[idx-1][0] > array[idx][0]:
            array[idx-1], array[idx] = array[idx], array[idx-1]
# 출력
for i, j in array:
    print(i, j)