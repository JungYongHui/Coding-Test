import math


def solution(progresses, speeds):
    answer = []

    dict1 = {i: 0 for i in range(1, len(progresses) + 1)}

    for idx, i in enumerate(progresses):
        dict1[idx + 1] = math.ceil((100 - i) / speeds[idx])

    dict_val = list(dict1.values())
    print(dict_val)

    front = 0
    for idx, i in enumerate(dict_val):
        if dict_val[idx] > dict_val[front]:
            answer.append(idx - front)
            front = idx
            print('front', front)
    answer.append(len(dict_val) - front)
    return answer