"""
피로도

link: https://programmers.co.kr/learn/courses/30/lessons/87946
"""
from itertools import permutations


def solution(k, dungeons):
    count = []
    dungeons = list(permutations(dungeons))

    for dungeon in dungeons:
        _k, _count = k, 0
        for required, cost in dungeon:
            if _k >= required:
                _k -= cost
                _count += 1
        count.append(_count)

    return max(count)
