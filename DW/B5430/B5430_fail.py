import sys
# 시간초과

# 테스트 케이스의 개수
input = int(sys.stdin.readline())

for _ in range(input):
# 처리 함수 목록
    func_input = list(sys.stdin.readline().rstrip())

    # 중간에 값하나 받음
    num = int(sys.stdin.readline())

    # 배열 받음
    num_input = sys.stdin.readline().rstrip()
    
    if num == 0:
        print('답: error')
        pass
    else:
        num_input = list(map(int, num_input[1:-1].split(',')))
        try:
            for i in func_input:
                if i == "R":
                    num_input.reverse()
                else:
                    del num_input[0]
            print('답: ',num_input)
        except:
            print('답: error')