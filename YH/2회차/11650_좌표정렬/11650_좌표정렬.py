import sys

n = int(sys.stdin.readline())

point_list = []
for i in range(n):
    point = list(map(int, sys.stdin.readline().rstrip().split()))
    point_list.append(point)

# 위의 for문은 입력값을 모두 아래의 주석 point_list와 같은 형식으로 만드는 작업임
# point_list = [[3, 4], [1, 1], [1, -1], [2, 2], [3, 3]]
##############################################################################
# < x좌표 기준으로 정렬 >

func = lambda x:x[0]
point_list.sort(key=func) # 1차적으로 리스트의 x좌표로 sorting 해줌
##############################################################################
# < 동일 x좌표의 경우 y좌표 기준으로 정렬 >

# 리스트를 x좌표 기준으로 묶은 dictionary로 변형함
point_dict = {i:[] for i,j in point_list}
for i,j in point_list:
    point_dict[i].append(j)

# dictionary에서 value들을 sorting함
for i in point_dict.values():
    i.sort()

# 출력하는 코드
for i in point_dict:
    for j in point_dict[i]:
        print(i, j)
