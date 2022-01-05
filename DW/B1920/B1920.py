# # 백준 1920
import sys

# 첫 번째, 두 번째 수들을 받기, 첫 번째는 set으로 받아야 시간이 단축됨
num1 = int(sys.stdin.readline())
arr1 = set(map(int, list(sys.stdin.readline().split())))
num2 = int(sys.stdin.readline())
arr2 = list(map(int, list(sys.stdin.readline().split())))

for i in arr2: # 두 번째로 입력받은 숫자를 하나씩 돈다.
    if i in arr1: # 첫 번째에 입력받은 숫자 무리에 포함되면 1 
        print(1)
    else:
        print(0)

 
