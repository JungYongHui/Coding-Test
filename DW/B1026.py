import sys

input = int(sys.stdin.readline())
li = list(sys.stdin.readline().split())
li2 = list(sys.stdin.readline().split())

# 문자열 -> 정수로 변환
li = list(map(int, li))
li2 = list(map(int, li2))

# 정렬
li.sort()
li2.sort()
# 역정렬
li2.reverse()


all_sum = 0
for i, j in enumerate(li):
    for ii, jj in enumerate(li2):
        if i == ii:
            sum = j * jj
            pass

    all_sum += sum
print(all_sum)

