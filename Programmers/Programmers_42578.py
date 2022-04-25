# Disguise
from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    return reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1


def My_solution(clothes):
    answer = 1
    dict_clothes = {}

    for i in clothes:
        if i[1] in dict_clothes:
            dict_clothes[i[1]] += 1
        else:
            dict_clothes[i[1]] = 1

    for item in dict_clothes.values():
        answer *= item+1

    return answer - 1