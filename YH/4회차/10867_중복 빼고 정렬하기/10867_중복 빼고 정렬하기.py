n = int(input())
origin = list(map(int, input().split()))
origin_set = list(set(origin))

origin_set.sort()
###############################################################################################
# << sort 와 sorted의 차이 >>

# sorted(a)는 새로운 정렬된 목록을 반환하며, 원래 목록은 영향을 받지 않는다.
# sorted(a)는 list뿐만 아니라 반복 가능한 모든 작업에 적용할 수 있음 ex)문자열, 튜플, 딕셔너리, 제너레이터
# b = sorted(a)

# a.sort()는 list를 그 자리에서 정렬하고 목록 인덱스를 변경하고 None을 반환

# list의 경우에 list.sort()는 복사본을 만들 필요가 없으므로 sorted()보다 빠름
###############################################################################################

# print(' '.join(origin_set))
# join 함수를 사용할 경우 runtime error가 뜬다. why??? ==> 주한이가 알려줄걸? ㅎㅎ
# join함수의 list를 순회하는 데 드는 시간 O(n)
print(*origin_set)