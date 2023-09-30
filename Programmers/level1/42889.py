"""
실패율

link: https://school.programmers.co.kr/learn/courses/30/lessons/42889
"""
from collections import Counter


def solution(N, stages):
    ratio = dict()
    count = Counter(stages)

    for stage in range(1, N + 1):
        users = sum([v for k, v in count.items() if k >= stage])
        nonclear = count[stage]

        try:
            ratio[stage] = nonclear / users
        except ZeroDivisionError:
            ratio[stage] = 0

    return sorted(ratio, key=lambda x: ratio[x], reverse=True)


N = [
    5,
    4,
]

stages = [
    [2, 1, 2, 6, 2, 4, 3, 3],
    [4, 4, 4, 4, 4],
]

for n, stage in zip(N, stages):
    print(solution(n, stage))
