N = int(input()) # 첫번째 인풋 개수 N
N_set = set(input().split(' ')) # N개의 자연수 input 리스트
# list의 요소 개수가 늘어날 수록 for문에서 시간을 많이 잡아먹는다.
# N 리스트 경우 중복된 요소가 필요가 없으므로, set로 중복 요소 제거 후 test


M = int(input()) # 두번째 인풋 개수 M
M_list = input().split(' ') # M개의 자연수 input 리스트

for i in M_list: # M 리스트의 요소 중
    if i in N_set: print(1) # set N의 요소랑 중복되는 것이 있으면 print(1)
    else: print(0) # 아니면 print(0)
