"""
튜플

link: https://school.programmers.co.kr/learn/courses/30/lessons/64065
"""


import re
from collections import Counter


def solution(s):
    s = Counter(re.findall("\d+", s))

    return [int(k) for k, v in s.most_common()]


S = [
    "{{2},{2,1},{2,1,3},{2,1,3,4}}",
    "{{1,2,3},{2,1},{1,2,4,3},{2}}",
    "{{20,111},{111}}",
    "{{123}}",
    "{{4,2,3},{3},{2,3,4,1},{2,3}}",
]

for data in S:
    print(solution(data))
