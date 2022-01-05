# 백준 15552 활용예제

import sys

#반복횟수를 n으로 정수를 받음.
n = int(sys.stdin.readline()) # stdin : input과 동일, readline : 읽고 다음줄
data = [sys.stdin.readline().strip() for i in range(n)] # strip 이어 붙이기.(split의 반대로가 생각하면 된다.)
print(data)
