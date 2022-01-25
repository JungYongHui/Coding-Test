import sys

n = int(input())

for _ in range(n):
    line = sys.stdin.readline().rstrip()

    answer = 0

    for i in line:
        if answer < 0:
            break
        if i == '(':
            answer += 1
        elif i == ')':
            answer -= 1

    if answer == 0:
        print('YES')
    else:
        print('NO')