import sys

input = int(sys.stdin.readline())

# 두 번째 입력값들 받는 리스트
input2_box = []
for _ in range(input):
    input2 = sys.stdin.readline().split()

    # 문자열 -> 정수로 변환
    input2 = list(map(int, input2))
    # 문자열 -> 정수로 변환2
    # func_int = lambda(x: int(X))
    # list(map(func_int, input2)

    input2_box.append(input2)
input2_box = sorted(input2_box)

for i in input2_box:
    print(i[0], i[1])

