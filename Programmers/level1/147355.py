"""
크기가 작은 부분 문자열

link: https://programmers.co.kr/learn/courses/30/lessons/147355
"""


def solution(t, p):
    subset = [
        True for i in range(len(t) - len(p) + 1) if int(t[i : i + len(p)]) <= int(p)
    ]

    return sum(subset)


t = ["3141592", "500220839878", "10203"]
p = ["271", "7", "15"]

for _t, _p in zip(t, p):
    print(solution(_t, _p))
