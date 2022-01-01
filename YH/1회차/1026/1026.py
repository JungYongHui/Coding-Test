import sys
import operator

n = int(sys.stdin.readline())

data1 = list(map(int,sys.stdin.readline().split()))
data2 = list(map(int,sys.stdin.readline().split()))

data1.sort()
data2.sort(reverse=True)

print(sum(map(operator.mul, data1, data2)))