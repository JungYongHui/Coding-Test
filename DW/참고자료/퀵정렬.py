# 시간: O(N*logN), 최악의 경우 O(N**2)
# 피벗기준으로 데이터를 비교한다.
# 왼쪽에선 피벗보다 큰 것, 오른쪽에선 피벗보다 작은 것을 찾아야함.*****
# 엇갈린다면 right와 pivot을 바꾸는 것!

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    
    # index라고 생각
    pivot = start # 설정, 피벗은 첫 번째 원소
    left = start + 1 # 왼쪽부터 인덱스 지정
    right = end # 오른쪽부터 인덱스 지정

    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    # 재귀함수 호출
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
