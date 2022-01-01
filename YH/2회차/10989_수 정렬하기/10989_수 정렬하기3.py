import sys

def sor(array):
    if len(array) <= 1:
        return array
    pivot = array[0] # 핏벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x<=pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x>pivot] # 분할된 오른쪽 부분
    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬이 재귀함수로 수행되고 전체 리스트 반환
    return sor(left_side)+[pivot]+sor(right_side)

n = int(input())

array = []
for i in range(n):
    el = int(sys.stdin.readline().rstrip())
    array.append(el)

# array.sort(reverse=False)
array = sor(array)

for i in array:
    print(i)