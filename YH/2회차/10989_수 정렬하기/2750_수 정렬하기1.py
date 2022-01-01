import sys

n = int(input())

array = []
for i in range(n):
    el = int(sys.stdin.readline().rstrip())
    array.append(el)

array.sort(reverse=False)

for i in array:
    print(i)