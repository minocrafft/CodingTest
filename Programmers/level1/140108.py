"""
문자열 나누기

link: https://programmers.co.kr/learn/courses/30/lessons/140108
"""
from collections import defaultdict


def solution(s):
    answer = 0
    _dict = defaultdict(lambda: 0)

    target = None
    for i, _s in enumerate(s):
        if target is None:
            target = _s

        _dict[_s] += 1
        count = sum([_dict[key] for key in _dict if key != target])

        if _dict[target] == count:
            answer += 1
            target, _dict = None, defaultdict(lambda: 0)

    if _dict:
        answer += 1

    return answer


s = [
    "banana",
    "abracadabra",
    "aaabbaccccabba",
]


for _s in s:
    print(solution(_s))
