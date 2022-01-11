import sys

input = tuple(map(int, sys.stdin.readline().split()))
# input[0] (현재 식탁에 앉아 있는 사람의 수)
# input[1] == K (현재 사람으로부터 K번째 사람을 죽임).

# 사람 수
people = [i for i in range(1, input[0]+1)]
K = input[1]

die_box = []

die = 0
next_die = K-1 # 파이썬 인덱스 고려
for _ in range(len(people)):
    die += next_die
    if die >= len(people):
        die = die%len(people) # 나머지를 die에 넣음

    die_box.append(people[die])
    people.remove(people[die])

print('<'+ str(die_box)[1:-1] + '>')