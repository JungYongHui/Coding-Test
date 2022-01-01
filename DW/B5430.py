import sys

# 시간을 줄이기 위해서 R과 D의 개수를 센 후 계산한다.
# ['RDD', 'RD, 'RRRRDD', 'RRRR'] 등 D에서 R로 바뀌는 시점을 기준으로 끊어 리스트를 형성한다.
# 리스트를 계속 돌면서, D에 갯수에 따라 배열을 제거하는데,
# "R이 짝수일 때 -> 왼쪽, R이 홀수일 때 -> 오른쪽" 을 제거한다.
# 마지막으로 R의 총 홀/짝 여부에 따라 reverse를 사용한다.


# 테스트 케이스 숫자 받기
input = int(sys.stdin.readline())

for _ in range(input):
    # 처리 함수 목록
    func_input = sys.stdin.readline().rstrip()

    # 중간에 값하나 받음
    num = int(sys.stdin.readline())

    # 배열 받음
    try:
        num_input = list(map(int, sys.stdin.readline().rstrip()[1:-1].split(',')))
    except:
        print("error")
        pass

    split_list = []
    first = True
    j = 0

    # step1
    for i in range(len(func_input)):
        try:
            if func_input[i]=="D" and func_input[i] != func_input[i+1]:
                # first
                if first is True:
                    split_list.append(func_input[:i+1]) # **
                    j = i+1 # i인덱스를 j에 저장
                    first = not first

                # middle
                else:
                    split_list.append(func_input[j:i+1]) # **
                    j=i+1 # i인덱스를 j에 저장
                    
        except:
            split_list.append(func_input)
            
    if j: # final
        split_list.append(func_input[j:])
        
        
    # step2
    for i in split_list:
        if len(func_input) >= len(num_input):
            print('error')
            break
        
        else:
            if i.count('R')%2 ==0 or i.count('R') == 0: # 왼쪽으로 제거
                delete = i.count('D')
                del num_input[:delete] # 여기서 c는 배열

            else: # 오른쪽으로 제거
                delete = i.count('D')
                del num_input[-(delete):]

            if func_input.count('R')%2 == 1:
                num_input.reverse()

            print(num_input)