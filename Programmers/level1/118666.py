"""
성격 유형 검사하기

link: https://school.programmers.co.kr/learn/courses/30/lessons/118666
"""
from collections import defaultdict


def solution(survey, choices):
    types = ["RT", "CF", "JM", "AN"]
    scores = [3, 2, 1, 0, 1, 2, 3]
    scoredict = defaultdict(int)

    for sv, choice in zip(survey, choices):
        neg, pos = sv

        if choice > 4:
            scoredict[pos] += scores[choice - 1]
        else:
            scoredict[neg] += scores[choice - 1]

    return "".join([t1 if scoredict[t1] >= scoredict[t2] else t2 for t1, t2 in types])


survey = [
    ["AN", "CF", "MJ", "RT", "NA"],
    ["TR", "RT", "TR"],
]
choices = [
    [5, 3, 2, 7, 5],
    [7, 1, 3],
]

for sv, choice in zip(survey, choices):
    print(solution(sv, choice))
