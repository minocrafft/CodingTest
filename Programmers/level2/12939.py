"""
최댓값과 최솟값

link: https://programmers.co.kr/learn/courses/30/lessons/12939
type: 구현
"""


def solution(s):
    s = list(map(int, s.split()))
    return " ".join(map(str, [min(s), max(s)]))


S = [
    "1 2 3 4",
    "-1 -2 -3 -4",
    "-1 -1",
]


for data in S:
    print(solution(data))
