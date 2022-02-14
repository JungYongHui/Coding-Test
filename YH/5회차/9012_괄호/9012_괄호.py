import sys

n = int(input())

for _ in range(n):
    line = sys.stdin.readline().rstrip()
    flag = True
    answer = 0

    for i in line:
        if answer < 0:
            flag = False
            break
        if i == '(':
            answer += 1
        elif i == ')':
            answer -= 1

    print(['NO', 'YES'][flag])

    # if answer == 0:
    #     print('YES')
    # else:
    #     print('NO')