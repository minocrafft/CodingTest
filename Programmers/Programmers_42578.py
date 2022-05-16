"""
    위장
    
    - 스파이의 옷 조합 구하기
    - 스파이가 가진 의상이 2차원 배열로 주어질 때 서로 다른 옷 조합의 수 return
"""

def solution(clothes):
    answer = 1
    dict_clothes = dict()

    # 각 옷의 종류가 몇가지 있는지 Dictionary에 저장
    for clothe in clothes:
        if clothe[1] in dict_clothes:
            dict_clothes[clothe[1]] += 1
        else:
            dict_clothes[clothe[1]] = 1

    # 조합을 구하는 방식으로 옷의 종류 구하기
    # ex) 악세사리가 2개일 경우: 경우의 수는 (미착용, 1번 착용, 2번 착용) 3가지가 되므로 +1을 해줌
    for item in dict_clothes.values():
        answer *= item + 1

    # 모두 미착용인 경우를 제외해줌
    return answer - 1


"""
# 다른 풀이
from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    return reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
"""