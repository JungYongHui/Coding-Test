from collections import Counter
from functools import reduce


def solution(clothes):
    #     cloth = {i[1]:0 for i in clothes}
    #     answer = 1

    #     for i, j in clothes:
    #         cloth[j] += 1
    #     # print(list(cloth.values()))

    #     for i in list(cloth.values()):
    #         answer *= (i+1)

    #     return answer - 1
    cloth = Counter([val for key, val in clothes])
    print(cloth)
    answer = reduce(lambda com, x: com * (x + 1), cloth.values(), 1)
    return answer - 1