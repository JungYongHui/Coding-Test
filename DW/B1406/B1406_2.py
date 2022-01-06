import sys

# 커서 -> 인덱스
# 인덱스에 해당하는 숫자 -> 박스
# insert를 활용한다.

f_input = list(str(sys.stdin.readline().rstrip()))
print(f_input)

index = len(f_input)-1
print('index: ', f_input[index])

# 커서 왼쪽에 추가 시킨다는 것은, index+1의 자리에 추가시킨 다는 것과 같다.

def P(x):
    return f_input.insert(index+1, x)

# 맨 앞
def L():
    if index 
    return f_input

# 맨 뒤
def D():
    return ~~