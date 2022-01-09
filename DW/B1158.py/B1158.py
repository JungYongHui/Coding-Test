import sys

input = list(map(int, sys.stdin.readline().split()))
print(input)
# input[0] (현재 식탁에 앉아 있는 사람의 수)
# input[1] == K (현재 사람으로부터 K번째 사람을 죽임).

people = list(range(1, input[0]+1))
print('people:', people)
K = input[1]
die_box = []
die = K # 첫 번째, 파이썬 인덱스 고려.

while len(die_box) != input[0]:
    if die <= len(people):
        die_person = people[die-1]
        
        die_box.append(die_person)
        people.remove(die_person)
        die += K
    else:
        die = die - len(people)
    print('die:', die)
print(die_box)