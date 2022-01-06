#%% import
import sys
input = sys.stdin.readline
#%% main
'''
S = A[0]×B[0] + ... + A[N-1]×B[N-1]의 최소값 S 구하기

큰거는 작은거랑, 작은 거는 큰거랑 매칭
'''
n = input() # n: 배열 A,B의 길이 N

a = input().split() # 배열 A
a = [int(i) for i in a]

b = input().split() # 배열 B
b = [int(i) for i in b]

# 답 구할때는 재배열 해도됨 ㅎㅎ
a.sort(reverse=True) # 크기 역순 정령
b.sort()    # 크기순으로 정렬

sum = 0
for i,j in zip(a,b):
    sum += i*j 

print(sum)