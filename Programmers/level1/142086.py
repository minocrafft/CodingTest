"""
가장 가까운 같은 글자

link: https://programmers.co.kr/learn/courses/30/lessons/142086
"""


def solution(s):
    answer = []
    _dict = dict()

    for i, _s in enumerate(s):
        if _s in _dict:
            answer.append(i - _dict[_s])
        else:
            answer.append(-1)

        _dict[_s] = i

    return answer


s = ["banana", "foobar"]

for _s in s:
    print(solution(_s))
